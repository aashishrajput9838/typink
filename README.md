# Auto TypeScript

A simple program that automatically types text at the current cursor position.

## Prerequisites

- Node.js (v14 or higher)
- npm (Node Package Manager)

## Installation

1. Clone this repository or download the files
2. Install dependencies:
```bash
npm install
```

## Usage

1. Run the program:
```bash
npm start
```

2. You'll have 5 seconds to place your cursor where you want the text to be typed
3. The program will automatically type the predefined text at the cursor position

## Customization

To change the text that will be typed, edit the `textToType` variable in `src/index.ts`.

To change the typing speed, modify the `delay` parameter in the `typeText` function call (default is 100ms).

## Building

To build the TypeScript files:
```bash
npm run build
```

## Note

This program uses the `robotjs` library which requires native dependencies. Make sure you have the necessary build tools installed on your system. 