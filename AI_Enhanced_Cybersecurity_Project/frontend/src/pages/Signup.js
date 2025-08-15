import React, {useState} from 'react';
import axios from 'axios';
import {useNavigate} from 'react-router-dom';

export default function Signup(){
  const [username,setUsername] = useState('');
  const [password,setPassword] = useState('');
  const nav = useNavigate();

  async function submit(e){
    e.preventDefault();
    try{
      const res = await axios.post('http://localhost:8000/auth/signup', {username, password});
      const token = res.data.access_token;
      localStorage.setItem('token', token);
      localStorage.setItem('username', username);
      nav('/dashboard');
    }catch(err){
      alert('Signup failed');
    }
  }

  return (
    <form onSubmit={submit} style={{maxWidth:400}}>
      <h2>Signup</h2>
      <input placeholder="username" value={username} onChange={e=>setUsername(e.target.value)} />
      <br/>
      <input placeholder="password" type="password" value={password} onChange={e=>setPassword(e.target.value)} />
      <br/>
      <button type="submit">Signup</button>
    </form>
  );
}
