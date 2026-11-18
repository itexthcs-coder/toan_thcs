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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang20_p4_b3_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tikz_sol = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (0,0) -- (5.8,0) node[below] {Sai số ($\\mu\\text{m}$)};
\\draw[->, line width=1pt] (0,0) -- (0,3.6) node[left] {Tần số tương đối (\\%%)};
\\foreach \\y/\\lbl in {0.7/10, 1.4/20, 2.1/30, 2.8/40, 3.5/50} {
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=4pt] {$\\lbl$};
}
\\draw[dashed, line width=1pt] (1.2,1.05) -- (2.4,2.45) -- (3.6,2.24) -- (4.8,1.26);
\\fill (1.2,1.05) circle (1pt) node[below right] {$15\\%%$};
\\fill (2.4,2.45) circle (1pt) node[below right] {$35\\%%$};
\\fill (3.6,2.24) circle (1pt) node[above right] {$32\\%%$};
\\fill (4.8,1.26) circle (1pt) node[above right] {$18\\%%$};
\\draw[line width=1pt] (1.2,1.96) -- (2.4,3.29) -- (3.6,1.26) -- (4.8,0.49);
\\fill (1.2,1.96) circle (1pt) node[above] {$28\\%%$};
\\fill (2.4,3.29) circle (1pt) node[above] {$47\\%%$};
\\fill (3.6,1.26) circle (1pt) node[below left] {$18\\%%$};
\\fill (4.8,0.49) circle (1pt) node[below] {$7\\%%$};
\\node[below] at (1.2,0) {$2,5$};
\\node[below] at (2.4,0) {$7,5$};
\\node[below] at (3.6,0) {$12,5$};
\\node[below] at (4.8,0) {$17,5$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Một nhà máy sản xuất linh kiện điện tử kiểm tra sai số kích thước (đơn vị: $\\mu\\text{m}$) của $200$ sản phẩm trước và sau khi bảo trì máy móc:
\\begin{itemize}
\\item \textbf{Trước bảo trì}: $[0; 5)$ có $30$ sản phẩm; $[5; 10)$ có $70$ sản phẩm; $[10; 15)$ có $64$ sản phẩm; $[15; 20)$ có $36$ sản phẩm.
\\item \textbf{Sau bảo trì}: $[0; 5)$ chiếm $28\\%%$; $[5; 10)$ chiếm $47\\%%$; $[10; 15)$ chiếm $18\\%%$; $[15; 20)$ chiếm $7\\%%$.
\\end{itemize}
Biết rằng sản phẩm đạt tiêu chuẩn xuất khẩu phải có sai số kích thước dưới $10\\;\\mu\\text{m}$.\\
a) Lập bảng tần số tương đối ghép nhóm cho mẫu số liệu trước bảo trì và vẽ chung hai đường gấp khúc tần số tương đối ghép nhóm (nét đứt cho trước bảo trì, nét liền cho sau bảo trì) trên cùng một hệ trục tọa độ.\\
b) Dựa vào biểu đồ và số liệu tính toán, hãy đánh giá hiệu quả của việc bảo trì máy móc đối với tỉ lệ sản phẩm đạt tiêu chuẩn xuất khẩu.''')

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Với cỡ mẫu $n = 200$, tần số tương đối trước bảo trì của các nhóm lần lượt là: $15\\%%$; $35\\%%$; $32\\%%$; $18\\%%$. Ta có bảng tổng hợp và biểu đồ đoạn thẳng kép:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Sai số ($\\mu\\text{m}$) & $[0; 5)$ & $[5; 10)$ & $[10; 15)$ & $[15; 20)$ \\\\
\\hline
Giá trị đại diện & $2,5$ & $7,5$ & $12,5$ & $17,5$ \\\\
\\hline
Trước bảo trì & $15\\%%$ & $35\\%%$ & $32\\%%$ & $18\\%%$ \\\\
\\hline
Sau bảo trì & $28\\%%$ & $47\\%%$ & $18\\%%$ & $7\\%%$ \\\\
\\hline
\\end{tabular}
\\end{center}
%s
\\item Tỉ lệ sản phẩm đạt tiêu chuẩn xuất khẩu (sai số dưới $10\\;\\mu\\text{m}$) trước bảo trì là $15\\%% + 35\\%% = 50\\%%$; sau bảo trì tăng lên $28\\%% + 47\\%% = 75\\%%$ (tăng thêm $25\\%%$). Đồng thời tỉ lệ sản phẩm sai số lớn ($[15; 20)$) giảm mạnh từ $18\\%%$ xuống còn $7\\%%$, chứng tỏ việc bảo trì máy móc đem lại hiệu quả rất cao.
\\end{enumEX}''' % (tikz_sol))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
