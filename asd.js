const add = (x, y) => x + y;
const add2 = (x) => (y) => x + y;
add(10, 20) // 한 번의 apply
add2(10)(20) // 두 번의 apply
console.log(add(10, 20))
console.log(add2(10)(20))
const max = (x, y) => x > y ? x : y
const add3 = (x, y, z) => x + y + z
console.log(max(20, 10))
console.log(add3(10, 20, 30))