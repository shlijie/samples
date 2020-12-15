
/*
 *Basic Types
*/
let isDone: boolean = false
let decimal: number = 6
let hex: number = 0xf00d
let binary: number = 0b1010
let octal: number = 0o744
let big: bigint = 100n
let color: string = "blue"
let list: number[] = [1, 2, 3]
let list2: Array<number> = [1, 2, 3]
let x: [string, number]
x = ["hello", 10]
// x = [10, "hello"] // WRONG

enum Color {
  Red,
  Green,
  Blue,
}
let c: Color = Color.Green

enum Color1 {
  Red = 1,
  Green,
  Blue,
}
enum Color2 {
  Up = "UP",
  Down = "DOWN",
  Left = "LEFT",
  Right = "RIGHT",
}


/*
 *Special types
*/
const elem = document.getElementById("elementId")! as HTMLInputElement

function combine(a: number | string, b: number | string): void {
  //logic to validate types and perform operations
}

function foo(color: 'yellow' | 'brown'){}

function error(msg: string): never {
  throw new Error("msg")
}

function message(msg: string): void {
  console.log("msg")
}

let input: unknown = 'aaaaaa'
//before assigning it we should check its type
if (typeof input === "string") {
  let name: string = input
  console.log(name)
}

let myinput: string = 'bbbbbb'
// let mylength1: number = (<string>input).length
// console.log((myinput as string).length)
let mylength2: number = (input as string).length

// declare function getValue(key: string): any
// const str: string = getValue("test")

/*
 *Interfaces
*/
interface User {
  name: string
  age: number
}

function displayPersonalInfo(user: User) {
  console.log(`Name: ${user.name} - Age: ${user.age}`)
}

interface Square {
  color?: string
  width?: number
}

interface Point {
  readonly x: number
  readonly y: number
}

let square: Square = {
  width: 14,
}

let a: number[] = [1, 2, 3, 4]
let ronumbers: ReadonlyArray<number> = a

// ronumbers[0] = 4 //WRONG! It cannot be assigned

//But it could be used for iterating over its values for reading purposes
for (const num of ronumbers) {
  console.log(num)
}

/*
 *Classes
*/
class Rectangle {
  height: number
  width: number

  constructor(h: number, w: number) {
    this.height = h
    this.width = w
  }
}

const rectangle = new Rectangle(200, 10)
console.log(rectangle.height)
console.log(rectangle.width)

/*
 *Generics
*/
function myMax<T>(x: T, y: T): T {
  return x > y ? x : y
}

let intMax = myMax<number>(12, 50)
console.log(intMax)
