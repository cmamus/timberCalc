import React, { useState } from "react";

import Tracionados from "./ElementosTracionados";
import Comprimidos from "./ElementosComprimidos";

import "../styles/mainMenu.css"

function MainMenu() {
  const [controle, setControle] = useState(0);
  
  function elementosTracionados() {
    setControle(1);
  }

  function elementosComprimidos() {
    setControle(2);
  }

  return(
    
      <div className="main-menu-container">
        {controle === 0 && (
          <div>
            <h1>Main Menu</h1>
            <button className="main-menu-button" onClick={elementosTracionados}>Elementos Tracionados e Flexotracionados</button>
            <button className="main-menu-button" onClick={elementosComprimidos}>Elementos Comprimidos e Flexotracomprimidos</button>
          </div>
        )}
      
        {controle === 1 && (
          <div>
            <Tracionados setControle={setControle} />          
          </div>
        )}

        {controle === 2 && (
          <div>
            <Comprimidos setControle={setControle} />          
          </div>
        )}
        
        {controle !== 0 && controle !== 1 && controle !== 2 &&(
          <div>
            <h1>Algo deu errado no controle</h1>
          </div>
        )}
      </div>
      
  );
}

export default MainMenu;