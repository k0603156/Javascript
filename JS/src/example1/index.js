class Circle {
  constructor(w, h) {
    this.el = document.createElement("div");
    this.width = w;
    this.height = h;
  }

  init() {
    this.el.className = "circle-container";
    this.el.style.width = appendPx(this.width);
    this.el.style.height = appendPx(this.height);
  }

  add(item) {
    this.el.appendChild(item);
  }

  addAll(items) {
    for (let item of items) {
      this.el.appendChild(item);
    }
  }

  append() {
    document.body.appendChild(this.el);
  }
}

class Square {
  constructor(w, h, v) {
    this.el = document.createElement("div");
    this.el.className = "square";
    this.el.style.backgroundImage = `url('${v}')`;
    this.el.style.backgroundSize = "100% 100%";
    this.width = w;
    this.height = h;
    this.init();
  }

  init() {
    this.el.style.width = appendPx(this.width);
    this.el.style.height = appendPx(this.height);
    this.el.style.position = "absolute";
  }

  updatePosition() {
    this.el.style.transform = `translate(${appendPx(this._x)}, ${appendPx(
      this._y
    )})`;
  }

  set x(v) {
    this._x = v;
    this.updatePosition();
  }

  set y(v) {
    this._y = v;
    this.updatePosition();
  }

  get x() {
    return this._x;
  }

  get y() {
    return this._y;
  }
}

class CircleList {
  constructor(parentSize, angle, count) {
    this.parentSize = parentSize;
    this.radius = this.parentSize / 2;
    this.count = count;
    this.angle = angle;
    this.positions = [];
  }

  init() {
    const dx = [1, -1];
    const dy = [-1, 1];
    const positions = this.positions;

    for (let i = this.angle; i >= 0; i -= this.angle / this.count) {
      const obj = {};
      obj.x = Math.floor(this.radius * Math.cos(degreesToRadians(i)));
      obj.y = Math.floor(this.radius * Math.sin(degreesToRadians(i)));
      positions.push(obj);
    }

    backtracking(positions, positions.length - 2, 0, 0);
    backtracking(positions, positions.length - 2, 1, 1);

    function backtracking(positions, start, end, c) {
      if (end <= start) {
        const obj = {};
        obj.x = positions[start].x * dx[c];
        obj.y = positions[start].y * dy[c];

        positions.push(obj);

        backtracking(positions, start - 1, end, c);
      }
    }
  }

  calcRelativeDistance(Shape, images) {
    this.items = this.positions.map((item, i) => {
      const square = new Shape(
        this.parentSize / 6,
        this.parentSize / 6,
        images[i]
      );
      square.x = item.x + this.radius - square.width / 2;
      square.y = item.y + this.radius - square.height / 2;
      return square;
    });
  }

  set elements(v) {
    this._elements = v;
  }

  get elements() {
    return this.items.map((item) => item.el);
  }
}

function next() {
  const squares = circleList.items;
  const end = squares.length - 1;
  const tempX = squares[0].x;
  const tempY = squares[0].y;

  for (let i = 0; i < end; i++) {
    const current = squares[i];
    const next = squares[i + 1];
    current.x = next.x;
    current.y = next.y;
  }

  squares[end].x = tempX;
  squares[end].y = tempY;
}

function prev() {
  const squares = circleList.items;
  const end = squares.length - 1;
  const tempX = squares[end].x;
  const tempY = squares[end].y;

  for (let i = end; i > 0; i--) {
    const current = squares[i];
    const next = squares[i - 1];
    current.x = next.x;
    current.y = next.y;
  }

  squares[0].x = tempX;
  squares[0].y = tempY;
}

function appendPx(n) {
  return n + "px";
}
function degreesToRadians(degrees) {
  const pi = Math.PI;
  return degrees * (pi / 180);
}

const width = 500;
const height = 500;
const angle = 90;
const viewCount = 4;
const images = [
  "https://images.unsplash.com/photo-1554350747-ec45fd24f51b?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
  "https://images.unsplash.com/photo-1552559789-17f06d186c0e?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
  "https://images.unsplash.com/uploads/14108632958755ac7f7f3/fe4a5cbf?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
  "https://images.unsplash.com/photo-1554521948-6891dbc1cde7?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
  "https://images.unsplash.com/photo-1518556737724-e362c03e8740?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
  "https://images.unsplash.com/photo-1509422007420-a57adf7b7fdf?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
  "https://images.unsplash.com/photo-1550123290-43d5edd06f27?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
  "https://images.unsplash.com/photo-1524010246915-297e8bb735e6?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
  "https://images.unsplash.com/photo-1547582281-b2cfb9e84a3e?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
  "https://images.unsplash.com/photo-1543147144-44589dd5bba7?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
  "https://images.unsplash.com/photo-1470073564688-bd3e07238084?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
  "https://images.unsplash.com/photo-1489769002049-ccd828976a6c?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjE0NTg5fQ",
];

const circle = new Circle(width, height);
const circleList = new CircleList(width, angle, viewCount - 1);
(() => {
  circle.init();
  circle.append();
  circleList.init();
  circleList.calcRelativeDistance(Square, images);
  circle.addAll(circleList.elements);
  document.getElementById("next-btn").addEventListener("click", next);
  document.getElementById("prev-btn").addEventListener("click", prev);
})();
