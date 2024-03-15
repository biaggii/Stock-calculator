import os, sys

from altair import value
from cycler import V
import gradio as gr
import numpy as np
import pandas as pd

demo = gr.Blocks()


def f_1(sl, ent, tp) -> float:
    return (ent - tp) / (sl - ent)


def btn_new_line_click(df: pd.DataFrame) -> pd.DataFrame:
    if len(df) > 0:
        df.loc[len(df.index)] = [df.iloc[-1, -1], 0, 0, 0, 0]
    print(df)
    return df


def btn_remove_line_click(df):
    if df.__len__() > 1:
        df.drop(index=df.index[-1], axis=0, inplace=True)
    return df


with demo:
    gr.Label(value='買vision pro 買豆豆機')
    with gr.Row():
        lbl_profit = gr.Number(value=1, label="Profit")
        lbl_principal = gr.Number(value=1, label="Principal")
        # lbl_risk = gr.Number(value=0, label="Risk")
        # lbl_risk_reward = gr.Number(value=0, label="Risk Reward")
        lbl_epoch = gr.Number(value=1, label="Epoch")
    with gr.Accordion(label="公式"):
        with gr.Column():
            gr.Label(value='(ENT - TP) / (SL - ENT) = 1')
            gr.Label(value='(ENT - TP) / (SL - ENT) = 1')
            gr.Label(value='(ENT - TP) / (SL - ENT) = 1')
            gr.Label(value='(ENT - TP) / (SL - ENT) = 1')
    with gr.Row():
        grDf = gr.DataFrame(
            headers=['Money', 'SL', 'ENT', 'TP', 'RES'],
            datatype=['number', 'number', 'number', 'number', 'number'],
            value=[[1, 12, 10, 4, 2]],
            col_count=5,
        )
    with gr.Row():
        btn_new_line = gr.Button("New Line")
        btn_calculate = gr.Button("Re Calculate")
        btn_remove_line = gr.Button("Remove Line")
        btn_clean = gr.Button("Clean all")

    btn_new_line.click(
        btn_new_line_click,
        inputs=[grDf],
        outputs=[grDf],
    )
    btn_remove_line.click(
        btn_remove_line_click,
        inputs=[grDf],
        outputs=[grDf],
    )


demo.launch(share=True)
