# -*- coding: utf-8 -*-
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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang10_p4_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r = random.randint(2, 6)

        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (90:1.7);
\\coordinate (M) at (45:1.7);
\\coordinate (B) at (0:1.7);
\\coordinate (N) at (-45:1.7);
\\coordinate (C) at (-90:1.7);
\\coordinate (P) at (-135:1.7);
\\coordinate (D) at (180:1.7);
\\coordinate (Q) at (135:1.7);
\\draw[line width=1pt] (O) circle (1.7);
\\draw[line width=1pt] (A)--(M)--(B)--(N)--(C)--(P)--(D)--(Q)--cycle;
\\draw[line width=1pt, dashed] (A)--(B)--(C)--(D)--cycle;
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (M) circle (1pt) node[above right] {$M$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (N) circle (1pt) node[below right] {$N$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (P) circle (1pt) node[below left] {$P$};
\\fill (D) circle (1pt) node[left] {$D$};
\\fill (Q) circle (1pt) node[above left] {$Q$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Cho đường tròn $(O; %s\\text{ cm})$ và điểm $A$ nằm trên đường tròn $(O)$ (như hình vẽ). \\
a) Nêu cách xác định các đỉnh $B, C, D$ của hình vuông $ABCD$ nội tiếp $(O)$ bằng các phép quay thuận chiều tâm $O$. \\
b) Từ hình vuông $ABCD$, tiếp tục sử dụng một phép quay tâm $O$ để xác định bốn điểm $M, N, P, Q$ sao cho $AMBNCPDQ$ là một bát giác đều. Giải thích vì sao $AMBNCPDQ$ là bát giác đều. %s'''
                         % (r, hinh_tikz))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\item Vì bốn đỉnh của hình vuông chia đường tròn $(O)$ thành $4$ cung nhỏ bằng nhau, mỗi cung có số đo bằng $\\frac{360^\\circ}{4} = 90^\\circ$ nên ta xác định các đỉnh $B, C, D$ như sau: \\
- Điểm $B$ là ảnh của điểm $A$ qua phép quay thuận chiều $90^\\circ$ tâm $O$. \\
- Điểm $C$ là ảnh của điểm $A$ qua phép quay thuận chiều $180^\\circ$ tâm $O$. \\
- Điểm $D$ là ảnh của điểm $A$ qua phép quay thuận chiều $270^\\circ$ tâm $O$.
\item Thực hiện phép quay thuận chiều $45^\\circ$ tâm $O$ biến các điểm $A, B, C, D$ lần lượt thành các điểm $M, N, P, Q$. \\
Giải thích: Khi đó tám điểm $A, M, B, N, C, P, D, Q$ cùng nằm trên đường tròn $(O)$ theo thứ tự thuận chiều kim đồng hồ và chia đường tròn thành $8$ cung nhỏ bằng nhau, mỗi cung có số đo bằng $45^\\circ$. Do đó đa giác lồi $AMBNCPDQ$ có $8$ cạnh bằng nhau (căng các cung bằng nhau) và $8$ góc trong bằng nhau (mỗi góc bằng $180^\\circ - 45^\\circ = 135^\\circ$), nên $AMBNCPDQ$ là một bát giác đều.
\end{enumEX}''')

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
