let fs = require('fs');
// let input = fs.readFileSync('test.txt').toString();
var input = fs.readFileSync('/dev/stdin').toString().trim();
const dic = { '10': 'A', '9': 'A', '8': 'B', '7': 'C', '6': 'D' }
a = input.substr(-10, input.length - 1)
if (a in dic) {
    console.log(dic[a])
} else {
    console.log('F')
}