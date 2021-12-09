import fs from 'fs'
import path, { dirname } from 'path'
import { fileURLToPath } from 'url'

import solution from './solution.mjs'

const __dirname = dirname(fileURLToPath(import.meta.url))
const input = fs.readFileSync(path.resolve(__dirname, 'input.txt'), 'utf8')

const parsedInput = solution.parseInput(input)

console.log('Task 1:', solution.task1(parsedInput))
console.log('Task 2:', solution.task2(parsedInput))
