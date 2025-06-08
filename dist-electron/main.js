"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
const electron_1 = require("electron");
const path = __importStar(require("path"));
const robot = __importStar(require("robotjs"));
let mainWindow = null;
function createWindow() {
    mainWindow = new electron_1.BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
            webSecurity: false
        },
        titleBarStyle: 'hidden',
        backgroundColor: '#202020'
    });
    // In development, load from localhost
    if (process.env.NODE_ENV !== 'production') {
        console.log('Loading development URL...');
        mainWindow.loadURL('http://localhost:3000');
        mainWindow.webContents.openDevTools();
        // Add error handling for page load
        mainWindow.webContents.on('did-fail-load', (event, errorCode, errorDescription) => {
            console.error('Failed to load:', errorCode, errorDescription);
        });
        mainWindow.webContents.on('did-finish-load', () => {
            console.log('Page loaded successfully');
        });
    }
    else {
        // In production, load the built files
        mainWindow.loadFile(path.join(__dirname, '../build/index.html'));
    }
}
electron_1.app.whenReady().then(createWindow);
electron_1.app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        electron_1.app.quit();
    }
});
electron_1.app.on('activate', () => {
    if (electron_1.BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});
// Handle typing text
electron_1.ipcMain.on('type-text', (event, { text, delay }) => {
    const lines = text.split('\n');
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        robot.typeString(line);
        robot.setKeyboardDelay(delay);
        if (i < lines.length - 1) {
            robot.keyTap('enter');
            robot.setKeyboardDelay(delay);
        }
    }
    event.reply('typing-complete');
});
