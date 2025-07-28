import Log from './pages/Log'
import Send from './pages/Send';
import { useState } from 'react'
import './App.css'


function App() {
  const [showLogs, setShowLogs] = useState(true);

  return (
    <>
      <div>
        <div className="w-1/2 mt-[3%] h-auto flex gap-[10px]">
              <button className="rounded-lg border border-transparent px-5 py-2.5 text-base font-medium bg-gray-100 text-black hover:bg-purple-700 transition-colors duration-200" onClick={() => setShowLogs((true))}> List and search logs </button>
              <button className="rounded-lg border border-transparent px-5 py-2.5 text-base font-medium bg-gray-100 text-black hover:bg-purple-700 transition-colors duration-200" onClick={() => setShowLogs((false))}> Send a log </button>
        </div>
        <div>
        {
          showLogs ?
          <Log />
          :
          <Send />
        }
        </div>
      </div>
    </>
  )
}

export default App
