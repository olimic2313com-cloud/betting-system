import React from "react";

export default function BetCard({bet}){
  const ev = (bet.prob - (1/bet.odds))*100;
  const hitRate = (bet.hit_rate/bet.games*100).toFixed(0);

  return (
    <div style={{background:"#1e293b",borderRadius:"15px",padding:"20px",marginBottom:"20px"}}>
      <div style={{display:"flex",alignItems:"center"}}>
        <img src={bet.image} alt="player" width="60" style={{borderRadius:"50%",marginRight:"15px"}}/>
        <div>
          <h3>{bet.player}</h3>
          <p>{bet.team} vs {bet.opponent}</p>
        </div>
      </div>

      <div style={{marginTop:"10px"}}>
        <p>📊 Probability: {bet.prob}</p>
        <p>💰 Odds: {bet.odds}</p>
        <p style={{color:"#22c55e"}}>EV: {ev.toFixed(1)}%</p>
        <p>Hit Rate: {bet.hit_rate}/{bet.games} ({hitRate}%)</p>
      </div>

      <div style={{display:"flex",gap:"5px",marginTop:"10px"}}>
        {[...Array(15)].map((_,i)=> (
          <div key={i} style={{width:"20px",height:"20px",background:i<bet.hit_rate?"#22c55e":"#ef4444"}}></div>
        ))}
      </div>
    </div>
  );
}
