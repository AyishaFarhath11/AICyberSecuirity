import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import Signup from './pages/Signup';
import Dashboard from './pages/Dashboard';
import Reports from './pages/Reports';

export default function App(){
  return (
    <div style={{fontFamily: 'Arial, sans-serif', padding: 20}}>
      <nav style={{marginBottom: 20}}>
        <Link to="/" style={{marginRight:10}}>Home</Link>
        <Link to="/dashboard" style={{marginRight:10}}>Dashboard</Link>
        <Link to="/reports" style={{marginRight:10}}>Reports</Link>
        <Link to="/login" style={{marginRight:10}}>Login</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/login" element={<Login/>} />
        <Route path="/signup" element={<Signup/>} />
        <Route path="/dashboard" element={<Dashboard/>} />
        <Route path="/reports" element={<Reports/>} />
      </Routes>
    </div>
  );
}
