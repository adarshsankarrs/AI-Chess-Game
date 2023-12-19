import chess
import chess.pgn
import chess.svg
import chess.engine
import random
import time
from math import log,sqrt,e,inf
from io import BytesIO
import numpy as np
import requests
import pandas as pd
from PIL import Image
from cairosvg import svg2png
import cv2
import streamlit as st

def app():
    class node():
        def __init__(self):
            self.state = chess.Board()
            self.action = ''
            self.children = set()
            self.parent = None
            self.N = 0
            self.n = 0
            self.v = 0

    def ucb1(curr_node):
        ans = curr_node.v+2*(sqrt(log(curr_node.N+e+(10**-6))/(curr_node.n+(10**-10))))
        return ans

    def rollout(curr_node):
        #Checking whether the current position of the node is checkmate
        if(curr_node.state.is_game_over()):
            board = curr_node.state
            if(board.result()=='1-0'):
                #print("h1")
                # st.header("Checkmate! White wins")
                return (1,curr_node)
            elif(board.result()=='0-1'):
                # st.header("Checkmate! Black wins")
                #print("h2")
                return (-1,curr_node)
            else:
                return (0.5,curr_node)
        
        all_moves = [curr_node.state.san(i) for i in list(curr_node.state.legal_moves)]
        
        for i in all_moves:
            tmp_state = chess.Board(curr_node.state.fen())
            tmp_state.push_san(i)
            child = node()
            child.state = tmp_state
            child.parent = curr_node
            curr_node.children.add(child)
        rnd_state = random.choice(list(curr_node.children))

        return rollout(rnd_state)

    def expand(curr_node,white):
        if(len(curr_node.children)==0):
            return curr_node
        max_ucb = -inf
        if(white):
            idx = -1
            max_ucb = -inf
            sel_child = None
            for i in curr_node.children:
                tmp = ucb1(i)
                if(tmp>max_ucb):
                    idx = i
                    max_ucb = tmp
                    sel_child = i

            return(expand(sel_child,0))

        else:
            idx = -1
            min_ucb = inf
            sel_child = None
            for i in curr_node.children:
                tmp = ucb1(i)
                if(tmp<min_ucb):
                    idx = i
                    min_ucb = tmp
                    sel_child = i

            return expand(sel_child,1)

    def rollback(curr_node,reward):
        curr_node.n+=1
        curr_node.v+=reward
        while(curr_node.parent!=None):
            curr_node.N+=1
            curr_node = curr_node.parent
        return curr_node

    def mcts_pred(curr_node,over,white,iterations=10):
        if(over):
            return -1
        all_moves = [curr_node.state.san(i) for i in list(curr_node.state.legal_moves)]
        map_state_move = dict()
        
        for i in all_moves:
            tmp_state = chess.Board(curr_node.state.fen())
            tmp_state.push_san(i)
            child = node()
            child.state = tmp_state
            child.parent = curr_node
            curr_node.children.add(child)
            map_state_move[child] = i
            
        while(iterations>0):
            if(white):
                idx = -1
                max_ucb = -inf
                sel_child = None
                for i in curr_node.children:
                    tmp = ucb1(i)
                    if(tmp>max_ucb):
                        idx = i
                        max_ucb = tmp
                        sel_child = i
                ex_child = expand(sel_child,0)
                reward,state = rollout(ex_child)
                curr_node = rollback(state,reward)
                iterations-=1
            else:
                idx = -1
                min_ucb = inf
                sel_child = None
                for i in curr_node.children:
                    tmp = ucb1(i)
                    if(tmp<min_ucb):
                        idx = i
                        min_ucb = tmp
                        sel_child = i

                ex_child = expand(sel_child,1)

                reward,state = rollout(ex_child)

                curr_node = rollback(state,reward)
                iterations-=1
        if(white):
            
            mx = -inf
            idx = -1
            selected_move = ''
            for i in (curr_node.children):
                tmp = ucb1(i)
                if(tmp>mx):
                    mx = tmp
                    selected_move = map_state_move[i]
            return selected_move
        else:
            mn = inf
            idx = -1
            selected_move = ''
            for i in (curr_node.children):
                tmp = ucb1(i)
                if(tmp<mn):
                    mn = tmp
                    selected_move = map_state_move[i]
            return selected_move

    st.header("A Game of Chess using Monte Carlo Tree Search")
    board = chess.Board()
    png = svg2png(bytestring=chess.svg.board(board))
    p1 = st.empty()
    imageLocation = st.empty()
    p3 = st.empty()
    p2 = st.empty()
    
    # Open png in PIL
    pil_img = Image.open(BytesIO(png)).convert('RGBA')
    cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGBA2BGRA)
    imageLocation.image(cv_img, caption='Initial pose', width=600)
    white = 1
    moves = 0
    pgn = []
    game = chess.pgn.Game()
    evaluations = []
    sm = 0
    cnt = 0
    df = pd.DataFrame(columns=['Turn','Moves by White','Moves by Black'])
    iteration=1
    #gameboard=display.start(board.fen())
    if st.button("Start"):
        if(st.button("stop game")):
            st.stop()
        while((not board.is_game_over())):
            print("Iteration",iteration)
            iteration+=1
            l  = 'Total number of moves: '+str(moves)
            p3.subheader(l)
            all_moves = [board.san(i) for i in list(board.legal_moves)]
            #start = time.time()
            if(white):
                p1.subheader("White's Turn")
                root = node()
                root.state = board
                result = mcts_pred(root,board.is_game_over(),white)
                df.loc[len(df.index)] = [iteration-1, result, 'No move'] 
                #sm+=(time.time()-start)
                board.push_san(result)
            else:
                p1.subheader("Black's Turn")
                root = node()
                root.state = board
                result = mcts_pred(root,board.is_game_over(),white)
                df.loc[len(df.index)] = [iteration-1, 'No move',result ] 
                #sm+=(time.time()-start)
                board.push_san(result)

            #display.start(board.fen())
            #print(result)
            p2.table(df)
            png = svg2png(bytestring=chess.svg.board(board))
            
            
        # Open png in PIL
            pil_img = Image.open(BytesIO(png)).convert('RGBA')
            cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGBA2BGRA)
            imageLocation.image(cv_img, caption="Move "+result,width=600)

        # gameboard=display.update(board.fen())
            pgn.append(result)
   
            white ^= 1
            moves+=1
      
        #display.terminate()
            #board_evaluation = evaluate(board.fen().split()[0])
            #evaluations.append(board_evaluation)
        #print("Average Time per move = ",sm/cnt)
