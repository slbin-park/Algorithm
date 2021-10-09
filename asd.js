// const add = (x, y) => x + y;
// const add2 = (x) => (y) => x + y;
// add(10, 20) // 한 번의 apply
// add2(10)(20) // 두 번의 apply
// console.log(add(10, 20))
// console.log(add2(10)(20))
// const max = (x, y) => x > y ? x : y
// const add3 = (x, y, z) => x + y + z
// console.log(max(20, 10))
// console.log(add3(10, 20, 30))
// var x = 1;
// function foo() {
//     var x = 10;
//     bar(x);
// }
// function bar(x) {
//     console.log(x)
// }
// foo();
// bar(x);
// function f1() { return this.lastName; }
// function f2(obj) {
//     console.log(obj)
//     return obj.fistName;
// }

// lastName = "Kim"

// const person = {
//     fistName: 'Geonho',
//     lastName,
//     getName: function () { return this.lastName + '' + this.fistName; },
//     getLastName: function () { return 'Mr' + this.lastName; },
//     f1
// };

// console.log(person.getName());
// console.log(person.getLastName());
// console.log(person.f1());
// console.log(f2(person));
var pizza = {
    name: '자바피자',
    radius: 10,


    getArea: function () { return this.radius * this.radius * 3.14; }
};
var dounts = {
    name: '자바 도넛',
    radius: 2,

    getArea: function () {
        console.log('rd : ', this.radius)
        return (this.radius * this.radius * 3.14);
    }
}

console.log(pizza.name + "의 면적은" + pizza.getArea())
console.log(dounts.name + "의 면적은 " + dounts.getArea())