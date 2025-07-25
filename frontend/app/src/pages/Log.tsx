import { useState, useEffect } from 'react'
import instance from '../axios/instance';
import './Log.css'


export default function Log()
{
  const [logs, setLogs] = useState(null);

  useEffect(() => {
    instance.get('/logs/search')
    .then(response => {
      setLogs(response.data)
    })
    .catch(error => {
      console.error(error);
    });
    return () => {};
  }, []);

  return (
    <>
      <h1>Log list</h1>
      <input type="text" placeholder="Search logs" />
    </>
  )
}