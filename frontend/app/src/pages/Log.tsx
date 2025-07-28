import { useState, useEffect } from 'react'
import instance from '../axios/instance';
import dayjs from 'dayjs';
import './Log.css';

import type { TLog, TSearchLog } from '../types/types';


export default function Log()
{
  const [data, setData] = useState<TLog[]>([]);
  const [filter, setFilter] = useState<TSearchLog>({
    q: '',
    level: '',
    service: '',
  });

  // Trigger le GET au montage du composant et quand modifications des valeurs du useState filter
  useEffect(() => {
    instance.get('/logs/search', {
      params: {
        q: filter?.q,
        level: filter?.level,
        service: filter?.service,
      },
    })
    .then(response => {
      setData(response.data)
    })
    .catch(error => {
      console.error(error);
    });
    return () => {};
  }, [filter]);

  return (
    <>
      <h1>Log list</h1>
      <div>
        <input className='mt-10 border border-gray-300' type="text" placeholder="Search for a log message" onChange={(e) => setFilter((prev) => ({...prev, q: e.target.value}))}/>
      </div>
      <div>
        <select className='mt-4 border rounded border-gray-300' defaultValue='' onChange={(e) => setFilter((prev) => ({...prev, level: e.target.value}))}>
            <option value="">- Filter level -</option>
            <option value="INFO">Info</option>
            <option value="WARNING">Warning</option>
            <option value="ERROR">Error</option>
            <option value="DEBUG">Debug</option>
        </select>
      </div>
      <div>
        <select className='mt-4 border rounded border-gray-300' defaultValue='' onChange={(e) => setFilter((prev) => ({...prev, service: e.target.value}))}>
          <option value="">- Filter service -</option>
          <option value="api-gateway">API Gateway</option>
          <option value="auth-service">Auth service</option>
          <option value="db-service">DB service</option>
          <option value="worker-service">Worker service</option>
          <option value="notification-service">Notification service</option>
        </select>
      </div>
      <div className="p-4 mt-5">
        <table className="min-w-full table-auto border border-gray-300 rounded-md">
          <thead className="bg-gray-100">
            <tr>
              <th className="px-4 py-2 border-b text-black">Timestamp</th>
              <th className="px-4 py-2 border-b text-black">Level</th>
              <th className="px-4 py-2 border-b text-black">Message</th>
              <th className="px-4 py-2 border-b text-black">Service</th>
            </tr>
          </thead>
          {
            data &&
            <tbody>
              {data.map((log) => (
                <tr key={log.id} className="hover:bg-purple-700">
                  <td className="px-4 py-2 border-b">{dayjs(log.timestamp).format('YYYY/MM/DD HH:mm')}</td>
                  <td className="px-4 py-2 border-b">{log.level}</td>
                  <td className="px-4 py-2 border-b">{log.message}</td>
                  <td className="px-4 py-2 border-b">{log.service}</td>
                </tr>
              ))}
            </tbody>
          }
        </table>
      </div>
    </>
  )
}