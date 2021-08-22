const type = (target, type) => {
	if (typeof type == "string") {
		if (typeof target != type)
			throw TypeError(`invaild type ${target} : ${type}`);
	} else if (!(target instanceof type))
		throw TypeError(`invaild type ${target} : ${type}`);
	return target;
};

const ViewModel = class {
	static #private = Symbol();
	static get(data) {
		return new ViewModel(this.#private, data);
	}
	styles = {};
	attributes = {};
	properties = {};
	events = {};
	constructor(checker, data) {
		if (checker != ViewModel.#private) throw "use ViewModel.get()";
		Object.entries(data).forEach(([k, v]) => {
			switch (k) {
				case "styles":
					this.styles = v;
					break;
				case "attributes":
					this.attributes = v;
					break;
				case "properties":
					this.properties = v;
					break;
				case "events":
					this.events = v;
					break;
				default:
					this[k] = v;
			}
		});
		Object.seal(this);
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

const Binder = class {
	#items = new Set();
	#processors = {};
	add(v, _ = type(v, BinderItem)) {
		this.#items.add(v);
	}
	addProcessor(v, _0 = type(v, Processor)) {
		this.#processors[v.cat] = v;
	}
	render(viewmodel, _ = type(viewmodel, ViewModel)) {
		const processores = Object.entries(this.#processors);
		this.#items.forEach((item) => {
			const vm = type(viewmodel[item.viewmodel], ViewModel), el = item.el;
			processores.forEach(([pk, processor]) => {
				Object.entries(vm[pk]).forEach(([k, v]) => {
					processor.process(vm, el, k, v);
				});
			});
		});
	}
};

const Processor = class {
	cat;
	constructor(cat) {
		this.cat = cat;
		Object.freeze(this);
	}
	z;
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

module.exports.type = type;

module.exports.ViewModel = ViewModel;
module.exports.BinderItem = BinderItem;
module.exports.Binder = Binder;
module.exports.Processor = Processor;
module.exports.Scanner = Scanner;
