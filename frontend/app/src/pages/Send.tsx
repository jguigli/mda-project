import { useState, useEffect } from 'react'
import instance from '../axios/instance';
import dayjs from 'dayjs';

import type { TSendLog } from '../types/types';


export default function Send()
{
  const [sendLog, setSendLog] = useState<TSendLog>({
    level: '',
    message: '',
    service: '',
  });

  const sendLogApi = () => {
    if ([sendLog.level, sendLog.message, sendLog.service].some(value => value === ''))
      return;
    instance.post('/logs', {
      timestamp: dayjs().toISOString(),
      level: sendLog.level,
      message: sendLog.message,
      service: sendLog.service,
    })
    .catch(error => {
    console.error(error);
    });
  }

  return (
    <>
      <h1>Send a log</h1>
      <div>
        <input className='mt-10 border rounded border-gray-300' type="text" placeholder="Message" onChange={(e) => setSendLog((prev) => ({...prev, message: e.target.value}))}/>
      </div>
      <div>
        <select className='mt-4 border rounded border-gray-300' defaultValue='' onChange={(e) => setSendLog((prev) => ({...prev, level: e.target.value}))}>
          <option value="">- Select a level -</option>
          <option value="INFO">Info</option>
          <option value="WARNING">Warning</option>
          <option value="ERROR">Error</option>
          <option value="DEBUG">Debug</option>
        </select>
      </div>
      <div>
        {/* <input className='mt-4 border rounded border-gray-300' type="text" placeholder="Service" onChange={(e) => setSendLog((prev) => ({...prev, service: e.target.value}))}/> */}
        <select className='mt-4 border rounded border-gray-300' defaultValue='' onChange={(e) => setSendLog((prev) => ({...prev, service: e.target.value}))}>
          <option value="">- Select a service -</option>
          <option value="api-gateway">API Gateway</option>
          <option value="auth-service">Auth service</option>
          <option value="db-service">DB service</option>
          <option value="worker-service">Worker service</option>
          <option value="notification-service">Notification service</option>
        </select>
      </div>
      <button 
      className="mt-5 rounded-lg border border-transparent px-5 py-2.5 text-base font-medium bg-gray-100 text-black hover:bg-purple-700 transition-colors duration-200"
      onClick={() => sendLogApi()}
      >
        Send
      </button>
    </>
  )
}