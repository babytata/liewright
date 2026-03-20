const display = document.getElementById('display');
let current = '';
let operator = '';
let operand = '';
let justCalculated = false;
let sequence = [];
let looping = false;

const soundMap = {
  '0': 'sounds/0.mp3',
  '1': 'sounds/1.mp3',
  '2': 'sounds/2.mp3',
  '3': 'sounds/3.mp3',
  '4': 'sounds/4.mp3',
  '5': 'sounds/5.mp3',
  '6': 'sounds/6.mp3',
  '7': 'sounds/7.mp3',
  '8': 'sounds/8.mp3',
  '9': 'sounds/9.mp3',
};

function playSound(num) {
  if (soundMap[num]) {
    const audio = new Audio(soundMap[num]);
    audio.currentTime = 0;
    audio.play().catch(err => console.warn("Sound play failed:", err));
  }
}

function updateDisplay(val) {
  display.textContent = val;
}

function playSequenceOnce(callback = null) {
  let i = 0;
  function playNext() {
    if (i >= sequence.length) {
      if (callback) callback();
      return;
    }
    playSound(sequence[i]);
    i++;
    setTimeout(playNext, 450);
  }
  playNext();
}

function loopSequence() {
  stopLoop();
  looping = true;
  function repeatLoop() {
    if (!looping) return;
    playSequenceOnce(() => {
      setTimeout(repeatLoop, 500);
    });
  }
  repeatLoop();
}

function stopLoop() {
  looping = false;
}

document.querySelectorAll('.btn[data-num]').forEach(btn => {
  btn.addEventListener('click', () => {
    if (justCalculated) {
      current = '';
      operator = '';
      operand = '';
      justCalculated = false;
    }
    const num = btn.dataset.num;
    current += num;
    updateDisplay(current);
    playSound(num);
  });
});

document.querySelectorAll('.btn.op').forEach(btn => {
  btn.addEventListener('click', () => {
    if (current === '') return;
    if (operator) return;
    operator = btn.dataset.op;
    operand = current;
    current = '';
    updateDisplay(operator);
  });
});

document.getElementById('clear').addEventListener('click', () => {
  current = '';
  operator = '';
  operand = '';
  justCalculated = false;
  updateDisplay('0');
  sequence = [];
  stopLoop();
});

document.getElementById('equals').addEventListener('click', () => {
  if (!operator || current === '' || operand === '') return;
  const a = parseFloat(operand);
  const b = parseFloat(current);
  let result = 0;
  switch (operator) {
    case '+': result = a + b; break;
    case '-': result = a - b; break;
    case '*': result = a * b; break;
    case '/': result = b !== 0 ? a / b : 'ERR'; break;
  }
  updateDisplay(result);
  justCalculated = true;
  sequence = result.toString().replace(/[^0-9]/g, '').split('');
  playSequenceOnce();
});

document.getElementById('play-seq').addEventListener('click', () => {
  if (sequence.length) {
    stopLoop();
    playSequenceOnce();
  }
});

document.getElementById('loop-seq').addEventListener('click', () => {
  if (sequence.length) loopSequence();
});

document.getElementById('stop-seq').addEventListener('click', () => {
  stopLoop();
});
