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

// 1415
// 아르고스 1600
// 발탄 노말 2500
// 1415
// 아르고스 1600
// 발탄 노말 2500
// 1415
// 아르고스 1600
// 발탄 노말 2500
// 1445
// 아르고스 1600
// 발탄 하드 4500
// 비아 노말 2500

// 1460
// 아르고스 1600
// 발탄 하드 4500
// 비아 하드 4500
// 1460
// 아르고스 1600
// 발탄 하드 4500
// 비아 하드 4500

// 아르고스 1600 : 6캐릭 9600
// 발탄 노말 2500 : 4캐릭 10000
// 발탄 하드 4500 : 3캐릭 13500
// 비아 노말 2500 : 1캐릭 2500
// 비아 하드 4500 : 2캐릭 9000