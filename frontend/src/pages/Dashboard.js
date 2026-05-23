import React, {useEffect, useState} from "react";
import axios from "axios";
import BetCard from "../components/BetCard";

export default function Dashboard(){
  const [bets,setBets] = useState([]);

  useEffect(()=>{
    axios.get("http://localhost:8000/bets")
      .then(res=>setBets(res.data));
  },[]);

  return (
    <div style={{background:"#0f172a",color:"white",padding:"20px"}}>
      <h1>🔥 Top Value Bets</h1>
      {bets.map((b,i)=> (
        <BetCard key={i} bet={b}/>
      ))}
    </div>
  );
}
