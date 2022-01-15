const mapValue = (target, block) => {
    return Object.fromEntries(
        Object.entries(target).map(([key, value]) => [key, block(value)])
    );
};
class Field {
    constructor(defaultValue) {
        const self = this;
        self.get = _ => self.v;
        self.set = newValue => {
            if(!self.typeValidation(newValue)) throw "invalid type: " + newValue;
            if(self.validator && !self.validator(newValue)) throw "invalid validation: " + newValue;
            self.v = newValue;
        }
    }
    default(v) {
        this.set(v);
    }
    toJSON() {
        return this.v;
    }
    fromJSON(v) {
        return v;
    }
    typeValidation() { 
        throw "must be override!";
    }
    validation(validator) {
        this.validator = validator;
        return this;
    }
};
class StringField extends Field {
    typeValidation(v) {
        return typeof v == "string";
    }
};
class StringListField extends Field {
    typeValidation(v) {
        return v instanceof Array && v.every(item => typeof item == "string");
    }
};
class NumberField extends Field {
    typeValidation(v) {
        return typeof v == "number";
    }
};
class NumberListField extends Field {
    typeValidation(v) {
        return v instanceof Array && v.every(item => typeof item == "number");
    }
};
class DateField extends Field {
    typeValidation(v) {
        return v instanceof Date;
    }
    toJSON() {
        if(this.v && 'toISOString' in this.v) return this.v.toISOString();
        return this.v;
    }
    fromJSON(v) {
        return new Date(v);
    }
};
class DateMapField extends Field {
    typeValidation(v) {
        return !(v instanceof Array) && typeof v == "object" && Object.values(v).every(item => item instanceof Date);
    }
    toJSON() {
        if(this.v && this.v instanceof Array) return mapValue(this.v, v => this.v, v => v.toISOString());
        return this.v;
    }
    fromJSON(v) {
        return mapValue(v, v => new Date(v));
    }
};
class EntityField extends Field {
    constructor(cls) {
        super();
        this.cls = cls;
    }
    typeValidation(v) {
        return v instanceof this.cls;
    }
    fromJSON(v) {
        const result = new this.cls;
        result.parse(v);
        return result;
    }
};
class EntityListField extends Field {
    constructor(cls) {
        super();
        this.cls = cls;
    }
    typeValidation(v) {
        return v instanceof Array && v.every(item => item instanceof this.cls);
    }
    fromJSON(v) {
        return v.map(json => (new this.cls).parse(json));
    }
};
class EntityMapField extends Field {
    constructor(cls) {
        super();
        this.cls = cls;
    }
    typeValidation(v) {
        return !(v instanceof Array) && typeof v == "object" && Object.values().every(item => item instanceof this.cls);
    }
    fromJSON(v) {
        return mapValue(v, json => (new this.cls).parse(json));
    }
};
class Entity {
    constructor() {
        Object.defineProperty(this, "_fields", {
            value: {},
            enumerable: false,
            writable: false,
            configurable: false,
        });
    }
    static union(base, ...sub) {
        if(!sub.every(cls=>cls.prototype instanceof base)) throw "invalid subclass";
        const parse = json => {
          let target;
          if(!sub.some(cls => {
            target = new cls;
            return Object.entries(target._fields).every(([key, field]) => {
              const jsonValue = json[key];
              if(jsonValue == undefined && field.get() === undefined) return false;
              else{
                target[key] = field.fromJSON(jsonValue);
                return true;
              }
            });
          })) throw "no matched sub class";
          return target;
        };
        Object.defineProperty(base, "parse", {
            enumerable: false,
            writable: false,
            configurable: false,
            value:parse,
        });
        Object.defineProperty(base.prototype, "parse", {
            enumerable: false,
            writable: false,
            configurable: false,
            value:parse,
        });
    }
    parse(json) {
        Object.entries(this._fields).forEach(([key, field]) => {
            const jsonValue = json[key];
            if(jsonValue == undefined) {
                if(field.get() === undefined) throw 'no key in json:' + key;
            } else this[key] = field.fromJSON(jsonValue); 
        });
        return this;
    }
    toJSON() {
        return this._fields;
    }
    define(field, descriptor) {
        Object.defineProperty(this, field, this._fields[field] = descriptor);
        return descriptor;
    }
    string(field) {
        return this.define(field, new StringField);
    }
    stringList(field) {
        return this.define(field, new StringListField);
    }
    number(field) {
        return this.define(field, new NumberField);
    }
    numberList(field) {
        return this.define(field, new NumberListField);
    }
    date(field) {
        return this.define(field, new DateField);
    }
    dateMap(field) {
        return this.define(field, new DateMapField)
    }
    entity(field, targetClass) {
        return this.define(field, new EntityField(targetClass));
    }
    entityList(field, targetClass) {
        return this.define(field, new EntityListField(targetClass));
    }
    entityMap(field, targetClass) {
        return this.define(field, new EntityMapField(targetClass));
    }
};
class Div extends Entity {
    constructor() {
        super();
        this.string("title");
    }
};
class Group extends Div {
    constructor() {
        super();
        this.entityList("sub", Div);
    }
};
class Team extends Div {
    constructor() {
        super();
        this.stringList("member");
    }
};
Entity.union(Div, Group, Team);
const div = Div.parse({
    "title": "개발실",
    "sub": [
        {
            "title": "FE팀",
            "sub": [
                {
                    "title": "FE팀1",
                    "member": ["kim", "oy"],
                },
            ],
        },
        {
            "title": "BE팀",
            "member": ["jin", "ji"],
        },
    ],
});
console.log(JSON.stringify(div));

//   div instanceof Group //true
// div.sub[0] instanceof Group //true
class Partner extends Entity {
    constructor() {
        super();
        this.string("name");
    }
};
class Member extends Entity {
    constructor() {
        super();
        this.string("name").validation(v => 2 <= v.length && v.length <= 10).default("___");
        this.number("age").validation(v => 15 <= v && v <= 50).default(15);
        this.date("birth");
        this.stringList("dev");
        this.dateMap('events');
        this.entity("partner", Partner);
        this.entityList("friends", Member);
    }
};

const member = new Member;
member.parse({
    name: "kim",
    age: 19,
    birth: "1992-11-27T00:00:00.000Z",
    dev: ['js'],
    events: {
        "sleep": "2000-01-01T00:00:00.000Z",
    },
    partner: {
        "name": "jin",
    },
    friends: [
        {
            name: "ji",
            age: 30,
            birth: "2000-01-01T00:00:00.000Z",
            dev: ['python'],
            events: {
                "sleep": "2000-01-01T00:00:00.000Z",
            },
            partner: {
                "name": "jin",
            },
            friends: [],
        },
        {
            name: "jin",
            age: 31,
            birth: "2000-01-01T00:00:00.000Z",
            dev: ['python'],
            events: {
                "sleep": "2000-01-01T00:00:00.000Z",
            },
            partner: {
                "name": "ji",
            },
            friends: [],
        }
    ]
});
console.log(JSON.stringify(member));