import Log from './pages/Log'
import Send from './pages/Send';
import { useState } from 'react'
import './App.css'


function App() {
  const [showLogs, setShowLogs] = useState(true);

  return (
    <>
      <div className='card'>
          <button className='button' onClick={() => setShowLogs((true))}> List and search logs </button>
      </div>
      <div className='card'>
          <button className='button' onClick={() => setShowLogs((false))}> Send a log </button>
      </div>
      {
        showLogs ?
        <Log />
        :
        <Send />
      }
    </>
  )
}

export default App
