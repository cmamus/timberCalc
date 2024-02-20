import React, { useState } from "react";
import Comprimidos from "./ElementosComprimidos";

import "../styles/mainMenu.css"
import Sidebar from "./Sidebar/Sidebar";

function MainMenu() {
  const [controle, setControle] = useState(0);
  
  function elementosComprimidos() {
    setControle(1);
  }

  return(
    <>
    <Sidebar />
    <div className="main-menu-container">
      {controle === 0 && (
        <div>
          <h1 className="main-menu-container">Main Menu</h1>
          <button className="main-menu-button" onClick={elementosComprimidos}>Elementos Comprimidos e Flexocomprimidos</button>
      </div>
      )}
      
      {controle === 1 && (
        <div>
          <Comprimidos setControle={setControle} />          
        </div>
      )}
        
      {controle !== 0 && controle !== 1 &&(
        <div>
          <h1>Algo deu errado no controle</h1>
        </div>
      )}
    </div>
    </>
  );
}

export default MainMenu;