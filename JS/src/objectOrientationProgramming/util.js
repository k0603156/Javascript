const type = (target, type) => {
	if (typeof type == "string") {
		if (typeof target != type)
			throw TypeError(`invaild type ${target} : ${type}`);
	} else if (!(target instanceof type))
		throw TypeError(`invaild type ${target} : ${type}`);
	return target;
};
const ViewModelListener = class {
	viewmodelUpdated(target, updated) {
		throw "override";
	}
};
const ViewModelValue = class {
	subKey;
	cat;
	k;
	v;
	constructor(subKey, cat, k, v) {
		this.subKey = subKey;
		this.cat = cat;
		this.k = k;
		this.v = v;
		Object.freeze(this);
	}
};

const ViewModel = class extends ViewModelListener {
	static get(data) {
		return new ViewModel(data);
	}
	static #subjects = new Set();
	static #inited = false;
	static notify(vm) {
		this.#subjects.add(vm);
		if (this.#inited) return;
		this.#inited = true;
		const f = (_) => {
			this.#subjects.forEach((vm) => {
				if (vm.#isUpdated.size) {
					vm.notify();
					vm.#isUpdated.clear();
				}
			});
			requestAnimationFrame(f);
		};
		requestAnimationFrame(f);
	}
	static define(vm, cat, obj) {
		return Object.defineProperties(
			obj,
			Object.entries(obj).reduce((r, [k, v]) => {
				r[k] = {
					enumerable: true,
					get: (_) => v,
					set: (newV) => {
						v = newV;
						vm.#isUpdated.add(new ViewModelValue(vm.subKey, cat, k, v));
					},
				};
				return r;
			}, {}),
		);
	}
	styles = {};
	attributes = {};
	properties = {};
	events = {};
	subKey = "";
	parent = null;
	#isUpdated = new Set();
	#listeners = new Set();
	constructor(data, _ = type(data, "object")) {
		super();
		Object.entries(data).forEach(([k, v]) => {
			if ("styles,attributes,properties".includes(k)) {
				if (!v || typeof v != "object") throw `invalid object k:${k}, v:${v}`;
				this[k] = ViewModel.define(this, k, v);
			} else {
				Object.defineProperty(this, k, {
					enumerable: true,
					get: (_) => v,
					set: (newV) => {
						v = newV;
						this.#isUpdated.add(new ViewModelValue(this.subKey, "", k, v));
					},
				});
				if (v instanceof ViewModel) {
					v.parent = this;
					v.subKey = k;
					v.addListener(this);
				}
			}
		});
		ViewModel.notify(this);
		Object.seal(this);
	}
	viewmodelUpdated(target, updated) {
		updated.forEach((v) => this.#isUpdated.add(v));
	}
	addListener(v, _ = type(v, ViewModelListener)) {
		this.#listeners.add(v);
	}
	removeListener(v, _ = type(v, ViewModelListener)) {
		this.#listeners.delete(v);
	}
	notify() {
		this.#listeners.forEach((v) =>
			v.viewmodelUpdated(this, this.#isUpdated),
		);
	}
};
const Scanner = class {
	scan(el, _ = type(el, HTMLElement)) {
		const binder = new Binder();
		this.checkItem(binder, el);
		const stack = [el.firstElementChild];
		let target;
		while ((target = stack.pop())) {
			this.checkItem(binder, target);
			if (target.firstElementChild) stack.push(target.firstElementChild);
			if (target.nextElementSibling) stack.push(target.nextElementSibling);
		}
		return binder;
	}
	checkItem(binder, el) {
		const vm = el.getAttribute("data-viewmodel");
		if (vm) binder.add(new BinderItem(el, vm));
	}
};
const Processor = class {
	cat;
	constructor(cat) {
		this.cat = cat;
		Object.freeze(this);
	}
	process(
		vm,
		el,
		k,
		v,
		_0 = type(vm, ViewModel),
		_1 = type(el, HTMLElement),
		_2 = type(k, "string"),
	) {
		this._process(vm, el, k, v);
	}
	_process(vm, el, k, v) {
		throw "override";
	}
};

const Binder = class extends ViewModelListener {
	#items = new Set();
	#processors = {};
	add(v, _ = type(v, BinderItem)) {
		this.#items.add(v);
	}
	viewmodelUpdated(target, updated) {
		const items = {};
		this.#items.forEach((item) => {
			items[item.viewmodel] = [
				type(target[item.viewmodel], ViewModel),
				item.el,
			];
		});
		updated.forEach((v) => {
			if (!items[v.subKey]) return;
			const [vm, el] = items[v.subKey],
				processor = this.#processors[v.cat];
			if (!el || !processor) return;
			processor.process(vm, el, v.k, v.v);
		});
	}
	addProcessor(v, _0 = type(v, Processor)) {
		this.#processors[v.cat] = v;
	}
	watch(viewmodel, _ = type(viewmodel, ViewModel)) {
		viewmodel.addListener(this);
		this.render(viewmodel);
	}
	unwatch(viewmodel, _ = type(viewmodel, ViewModel)) {
		viewmodel.removeListener(this);
	}
	render(viewmodel, _ = type(viewmodel, ViewModel)) {
		const processores = Object.entries(this.#processors);
		this.#items.forEach((item) => {
			const vm = type(viewmodel[item.viewmodel], ViewModel),
				el = item.el;
			processores.forEach(([pk, processor]) => {
				Object.entries(vm[pk]).forEach(([k, v]) => {
					processor.process(vm, el, k, v);
				});
			});
		});
	}
};
const BinderItem = class {
	el;
	viewmodel;
	constructor(
		el,
		viewmodel,
		_0 = type(el, HTMLElement),
		_1 = type(viewmodel, "string"),
	) {
		this.el = el;
		this.viewmodel = viewmodel;
		Object.freeze(this);
	}
};

module.exports.type = type;

module.exports.ViewModel = ViewModel;
module.exports.BinderItem = BinderItem;
module.exports.Binder = Binder;
module.exports.Processor = Processor;
module.exports.Scanner = Scanner;
