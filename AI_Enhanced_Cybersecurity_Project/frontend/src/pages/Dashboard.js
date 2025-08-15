import React, {useState} from 'react';
import axios from 'axios';

export default function Dashboard(){
  const [file, setFile] = useState(null);
  const [analysis, setAnalysis] = useState(null);

  async function upload(e){
    e.preventDefault();
    if(!file) return alert('Choose file');
    const form = new FormData();
    form.append('file', file);
    try{
      const res = await axios.post('http://localhost:8000/ingest/', form, {
        headers: {'Content-Type': 'multipart/form-data'}
      });
      alert(res.data.message);
    }catch(err){
      alert('Upload failed');
    }
  }

  async function runAnalysis(){
    try{
      const res = await axios.post('http://localhost:8000/analyze/', {data: {example: 'run analysis'}} );
      setAnalysis(res.data);
    }catch(err){
      alert('Analysis failed');
    }
  }

  return (
    <div>
      <h2>Dashboard</h2>
      <form onSubmit={upload}>
        <input type="file" onChange={e=>setFile(e.target.files[0])} />
        <br/>
        <button type="submit">Upload Logs / PCAP</button>
      </form>
      <hr/>
      <button onClick={runAnalysis}>Run Quick Analysis</button>
      {analysis && (
        <div style={{marginTop:20}}>
          <h3>Analysis Result</h3>
          <pre>{JSON.stringify(analysis, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
