import { useState } from 'react';

function Square({value, onSquareClick}) {
  return (
    <button className="square" onClick={onSquareClick}>
      {value}
    </button>
  );
}
function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}
export default function Board() {
  const [move, setMove] = useState(1);
  const [xIsNext, setXIsNext] = useState(true);
  const [squares, setSquares] = useState(Array(9).fill(null));
  const [firstClick, setFirstClick] = useState(null);

  function handleClick(i) {
    const nextSquares = squares.slice();
    let char;
    if(xIsNext){
      char = "X";
    }else{
      char = "O";
    }

    if(calculateWinner(squares)){return;}

    if(move >6){
      //if it is the first click
      if(firstClick === null){
        if((char === nextSquares[i])){
          setFirstClick(i);
        }
        return;
        //if it is the second click
      }else{
        if(nextSquares[i] === null){

          const row1 = Math.floor(i / 3);
          const col1 = i % 3;
          const row2 = Math.floor(firstClick / 3);
          const col2 = firstClick % 3;
          // Max distance of 1 in either row or column (including diagonals)
          if(!(Math.abs(row1 - row2) <= 1 && Math.abs(col1 - col2) <= 1)){
            setFirstClick(null);
            return;
          } 

          //set the squares temporarily
          let middle = nextSquares[4]
          nextSquares[firstClick] = null;
          nextSquares[i] = char;

          //If the char needs to move from the center of the board or win
          if(char === middle){
            //if this new arragment of squares:
            // 1. does not win
            // 2. does not vacate the center space
            // then return, and reset the board + first click
            if(calculateWinner(nextSquares) !== char){
              if(char === nextSquares[4]){
                nextSquares[firstClick] = char;
                nextSquares[i] = null;
                setSquares(nextSquares);
                setFirstClick(null);
                return;
              }
            }
          }

          //Standard case
          setSquares(nextSquares);
          setFirstClick(null);
          setXIsNext(!xIsNext);
          setMove((move+1));
          return;
        }
        setFirstClick(null);
        return;
      }
    }else{
      if(squares[i]){return;}
        nextSquares[i] = char;
    }
    setMove((move+1));
    setXIsNext(!xIsNext);
    setSquares(nextSquares);
  }

  const winner = calculateWinner(squares);
  let status;
  if (winner) {
    status = 'Winner: ' + winner;
  } else {
    status = 'Next player: ' + (xIsNext ? 'X' : 'O');
  }

  return (
    <>
      <div className="status">{status}</div>
      <div className="board-row">
        <Square value={squares[0]} onSquareClick={() => handleClick(0)} />
        <Square value={squares[1]} onSquareClick={() => handleClick(1)} />
        <Square value={squares[2]} onSquareClick={() => handleClick(2)} />
      </div>
      <div className="board-row">
        <Square value={squares[3]} onSquareClick={() => handleClick(3)} />
        <Square value={squares[4]} onSquareClick={() => handleClick(4)} />
        <Square value={squares[5]} onSquareClick={() => handleClick(5)} />
      </div>
      <div className="board-row">
        <Square value={squares[6]} onSquareClick={() => handleClick(6)} />
        <Square value={squares[7]} onSquareClick={() => handleClick(7)} />
        <Square value={squares[8]} onSquareClick={() => handleClick(8)} />
      </div>
    </>
  );
}

