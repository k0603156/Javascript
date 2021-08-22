const { type, ViewModel, BinderItem, Binder, Processor, Scanner } = require("./util.js");

(() => {
	const viewmodel = ViewModel.get({
		changeContents() {
			this.wrapper.styles.background = `rgb(
                    ${parseInt(Math.random() * 150) + 100},
                    ${parseInt(Math.random() * 150) + 100},
                    ${parseInt(Math.random() * 150) + 100}
                )`;
			this.contents.properties.innerHTML = Math.random()
				.toString(16)
				.replace(".", "");
		},
		wrapper: ViewModel.get({
			isStop: false,
			styles: {
				width: "50%",
				background: "#ffa",
				cursor: "pointer",
			},
			events: {
				click(e, vm) {
					vm.isStop = true;
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
				innerHTML: "contents",
			},
		}),
	});
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
				el[k] = v;
			}
		})("properties"),
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
				el["on" + k] = (e) => v.call(el, e, vm);
			}
		})("events"),
	);

	const f = (_) => {
		viewmodel.changeContents();
		binder.render(viewmodel);
		if (!viewmodel.wrapper.isStop) requestAnimationFrame(f);
	};
	requestAnimationFrame(f);
})();
