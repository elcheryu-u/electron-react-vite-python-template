const { app, BrowserWindow } = require('electron');
const path = require('node:path');
const { spawn } = require('child_process');


const isDev = process.env.NODE_ENV === 'development' || !app.isPackaged;

// Handle creating/removing shortcuts on Windows when installing/uninstalling.
if (require('electron-squirrel-startup')) {
  app.quit();
}

let mainWindow;
let flaskProcess;

const createWindow = () => {
  // Create the browser window.
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
  });

  // and load the index.html of the app.
  /* mainWindow.loadFile(path.join(__dirname, 'index.html')); */

  if (isDev) {
    // Open the DevTools.
    mainWindow.webContents.openDevTools();
    mainWindow.loadURL('http://localhost:5173');
  } else {
    mainWindow.loadFile(path.join(__dirname, '../../dist/renderer/index.html'));
  }

  mainWindow.on('closed', () => {
    mainWindow = null;
  })
};

function startFlask() {
  console.log('isDev', isDev)

  const flaskPath = isDev
    ? path.join(__dirname, '../../backend/app.py')
    : path.join(process.resourcesPath, 'app');

  const flaskExec = isDev ? 'python' : flaskPath;
  const args = isDev ? [flaskPath] : [];

  flaskProcess = spawn(flaskExec, args, {
    env: {
      ...process.env,
      FLASK_ENV: 'development',
    },
  });

  flaskProcess.stdout.on('data', (data) => {
    console.log(`Flask: ${data}`);
  });

  flaskProcess.stderr.on('data', (data) => {
    console.error(`Flask Error: ${data}`);
  });
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
  startFlask();
  createWindow();

  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});


const killFlask = () => {
  if (flaskProcess && !flaskProcess.killed) {
    flaskProcess.kill('SIGTERM');
    console.log('Flask process terminated.');
  }
};

app.on('before-quit', killFlask);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});


// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and import them here.

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});