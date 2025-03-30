import React, { useState } from 'react'
import CodeEditor from './components/CodeEditor'
import './App.css'

function App() {
  const [code, setCode] = useState('// Write your code here')
  const [output, setOutput] = useState('')

  const handleSubmit = async (action) => {
    try {
      const response = await fetch(`http://localhost:5000/${action}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code }),
      })
      const data = await response.json()
      setOutput(data.message)
    } catch (error) {
      console.error('Error:', error)
    }
  }

  return (
    <div className="App">
      <h1>AI Dev Lab</h1>
      <CodeEditor code={code} setCode={setCode} />
      <div className="actions">
        <button onClick={() => handleSubmit('refactor')}>Refactor</button>
        <button onClick={() => handleSubmit('doc')}>Generate Docstrings</button>
        <button onClick={() => handleSubmit('test')}>Write Unit Tests</button>
      </div>
      <div className="output">
        <h2>Output</h2>
        <pre>{output}</pre>
      </div>
    </div>
  )
}

export default App
