import * as robot from 'robotjs';

// Function to simulate typing text
function typeText(text: string, delay: number = 100): void {
    // Split the text into individual characters
    const characters = text.split('');
    
    // Type each character with a delay
    characters.forEach((char) => {
        robot.typeString(char);
        robot.setKeyboardDelay(delay);
    });
}

// Function to start auto-typing
function startAutoTyping(): void {
    console.log('Auto-typing will start in 5 seconds...');
    console.log('Please place your cursor where you want the text to be typed.');
    
    // Wait for 5 seconds before starting
    setTimeout(() => {
        const textToType = "This is an automatically typed text. You can modify this text in the code.";
        console.log('Starting to type...');
        typeText(textToType);
        console.log('Finished typing!');
    }, 5000);
}

// Start the program
console.log('Auto-typing program started.');
console.log('Press Ctrl+C to exit.');
startAutoTyping(); 