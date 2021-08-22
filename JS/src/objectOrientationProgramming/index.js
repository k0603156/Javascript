const {
	ViewModel,
	Processor,
	Scanner,
} = require("./util.js");

(() => {
	const scanner = new Scanner();
	const binder = scanner.scan(document.querySelector("#target"));
	binder.addProcessor(
		new (class extends Processor {
			_process(vm, el, k, v) {
				el.style[k] = v;
			}
		})("styles"),
	);
	binder.addProcessor(
		new (class extends Processor {
			_process(vm, el, k, v) {
				el.setAttribute(k, v);
			}
		})("attributes"),
	);
	binder.addProcessor(
		new (class extends Processor {
			_process(vm, el, k, v) {
				el[k] = v;
			}
		})("properties"),
	);
	binder.addProcessor(
		new (class extends Processor {
			_process(vm, el, k, v) {
				el["on" + k] = (e) => v.call(el, e, vm);
			}
		})("events"),
	);
	const viewmodel = ViewModel.get({
		isStop: false,
		changeContents() {
			this.wrapper.styles.background = `rgb(${
				parseInt(Math.random() * 150) + 100
			},${parseInt(Math.random() * 150) + 100},${
				parseInt(Math.random() * 150) + 100
			})`;
			this.contents.properties.innerHTML = Math.random()
				.toString(16)
				.replace(".", "");
		},
		wrapper: ViewModel.get({
			styles: {
				width: "50%",
				background: "#ffa",
				cursor: "pointer",
			},
			events: {
				click(e, vm) {
					vm.parent.isStop = true;
				},
			},
		}),
		title: ViewModel.get({
			properties: {
				innerHTML: "Title",
			},
		}),
		contents: ViewModel.get({
			properties: {
				innerHTML: "Contents",
			},
		}),
		input: ViewModel.get({
			properties: {
				value: "Title",
			},
			events: {
				input(e, vm) {
					if (e.isComposing) return;
					vm.properties.value = e.target.value;
				},
				blur(e, vm) {
					vm.properties.value = e.target.value.trim();
				},
			},
		}),
	});
	binder.watch(viewmodel);
	const f = (_) => {
		viewmodel.changeContents();
		if (!viewmodel.isStop) requestAnimationFrame(f);
	};
	requestAnimationFrame(f);
})();
