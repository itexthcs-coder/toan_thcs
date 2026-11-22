import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang14_p3_b2_c3_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        canh_tg = random.randint(8, 15)
        ma = random.randint(4, 8)
        kq = canh_tg + ma
        kq_str = str(kq)

        hinh_ve = '''
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (2,3.46);
        \\coordinate (B) at (0,0);
        \\coordinate (C) at (4,0);
        \\coordinate (M) at (1.8,1.3);
        \\coordinate (P) at (1.05,1.82);
        \\coordinate (Q) at (2.55,0);
        \\coordinate (R) at (2.55,2.51);
        \\draw[line width=1pt] (A)--(B)--(C)--(A) (P)--(R);
        \\draw[line width=1pt, dashed] (M)--(P) (M)--(Q) (M)--(R) (M)--(A);
        \\fill (A) circle (1pt) node[above] {$A$};
        \\fill (B) circle (1pt) node[below left] {$B$};
        \\fill (C) circle (1pt) node[below right] {$C$};
        \\fill (M) circle (1pt) node[below left] {$M$};
        \\fill (P) circle (1pt) node[left] {$P$};
        \\fill (Q) circle (1pt) node[below] {$Q$};
        \\fill (R) circle (1pt) node[right] {$R$};
        \\end{tikzpicture}
        \\end{center}'''

        noidungcauhoi = ('''Cho điểm $M$ nằm trong tam giác đều $ABC$ có cạnh bằng $%s\\text{ cm}$. Qua $M$ kẻ các đường thẳng song song với $BC$, $CA$, $AB$ lần lượt cắt $AB$, $BC$, $CA$ tại $P$, $Q$, $R$ (như hình vẽ). Biết $MA = %s\\text{ cm}$, tính tổng độ dài $AP + AR + PR$ (đơn vị: $\\text{cm}$). %s'''
                         % (canh_tg, ma, hinh_ve))

        loigiai = ('''Tứ giác $APMR$ là hình thang cân nên hai đường chéo bằng nhau: $PR = MA = %s\\text{ cm}$, và hai cạnh bên bằng nhau: $AP = MR$.\\\\
                   Mặt khác, tứ giác $MRCQ$ có $MR // CQ$ và $\\widehat{MRC} = \\widehat{C} = 60^\\circ$ (hoặc $\\triangle MRC$? Ta có $MR // AB$, $MQ // AC$ nên $\\widehat{RMC} = \\widehat{A} = 60^\\circ$, $\\widehat{RCM} = 60^\\circ$? Chính xác: $MR // AB$ nên $\\widehat{MRC} = 180^\\circ - 60^\\circ = 120^\\circ$, còn $\\triangle QMC$ đều nên $QM = QC$, và $MR = RC$ vì $\\widehat{RMC} = \\widehat{RCM}$ không đúng; chính xác là $APMR$ là hình thang cân có $AP = MR$, và $MQ // AC, MR // AB$? Không, $MP // BC$ và $AB$ cắt $MP$ tại $P$, $MQ // AC$ cắt $BC$ tại $Q$, $MR // AB$ cắt $AC$ tại $R$: trong hình bình hành? Không, $MR // AB$ nên $MR = PB$ không; $\\triangle APM$? Không, $AP + AR = MR + AR = RC + AR = AC = %s\\text{ cm}$ vì $MR = RC$ do $\\widehat{RMC} = \\widehat{B}$? Ta có $MR // AB$ và $MQ // AC$ nên $\\widehat{QMR} = \\widehat{A} = 60^\\circ$, và $RC // QM$? Đúng: $QM // AC$ tức $QM // RC$, còn $MR // AB$ nên $\\widehat{MRQ} = ...$ không, $RC$ và $QM$ song song, mà $CRMQ$ là hình thang cân có $MR = QC$? Không, $CRMQ$ có $QM // RC$ nên hai đáy là $QM$ và $RC$, hai cạnh bên là $MR$ và $CQ$ nên $MR = CQ$! Còn $BQMP$ có hai đáy $MP // BQ$ nên hai cạnh bên $BP = MQ$. Mà $\\triangle MQR$? Không, ở đây $AP = MR$ và $AR = AC - RC$... Khoan: trong hình thang cân $APMR$, hai đáy là $PM$ và $AR$, hai cạnh bên là $AP$ và $MR$ nên $AP = MR$! Lại có $MR // AB$ và $AC$ cắt chúng nên $\\widehat{MRC} = 180^\\circ - 60^\\circ = 120^\\circ$... Thực tế $MR = RC$ chỉ đúng nếu $\\triangle MRC$ cân tại $R$, mà $\\widehat{RCM} < 60^\\circ$ nên $MR \\neq RC$!).''' % (ma, canh_tg))
        # Thay bằng bài toán hoàn toàn chuẩn xác từ Bài 3.12: cho MA, MB, MC tìm chu vi tam giác PQR (câu 14) và cho chu vi PQR, MA, MB tìm MC (câu 15)!
        mb = random.randint(5, 9)
        mc = random.randint(6, 10)
        chu_vi = ma + mb + mc
        kq_str = str(chu_vi)

        noidungcauhoi = ('''Cho điểm $M$ nằm trong tam giác đều $ABC$. Qua $M$ kẻ các đường thẳng song song với $BC$, $CA$, $AB$ lần lượt cắt $AB$, $BC$, $CA$ tại $P$, $Q$, $R$ (như hình vẽ). Biết $MA = %s\\text{ cm}$, $MB = %s\\text{ cm}$, $MC = %s\\text{ cm}$. Tính chu vi của tam giác $PQR$ (đơn vị: $\\text{cm}$). %s'''
                         % (ma, mb, mc, hinh_ve))

        loigiai = ('''Các tứ giác $APMR$, $BQMP$, $CRMQ$ đều là hình thang cân nên hai đường chéo của mỗi hình thang cân bằng nhau:\\\\
                   $PR = MA = %s\\text{ cm}$, $PQ = MB = %s\\text{ cm}$, $QR = MC = %s\\text{ cm}$.\\\\
                   Chu vi của tam giác $PQR$ là: $PQ + QR + RP = %s + %s + %s = %s\\text{ cm}$.\\\\
                   Vậy chu vi tam giác $PQR$ bằng $%s\\text{ cm}$.'''
                   % (ma, mb, mc, mb, mc, ma, kq_str, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
