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


def bt_dang16_p4_b1_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.randint(5, 15)

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (130:1.8);
\\coordinate (B) at (10:1.8);
\\coordinate (C) at (-130:1.8);
\\coordinate (D) at (-10:1.8);
\\coordinate (H) at ($(A)!0.5!(B)$);
\\coordinate (K) at ($(C)!0.5!(D)$);
\\coordinate (I) at (1.18,0);
\\draw[line width=1pt] (O) circle (1.8);
\\draw[line width=1pt] (A)--(B) (C)--(D);
\\draw[line width=1pt, dashed] (O)--(H) (O)--(K) (-2.1,0)--(2.1,0);
\\fill (O) circle (1pt) node[above left] {$O$};
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below left] {$C$};
\\fill (D) circle (1pt) node[below right] {$D$};
\\fill (H) circle (1pt) node[above right] {$H$};
\\fill (K) circle (1pt) node[below right] {$K$};
\\fill (I) circle (1pt) node[above] {$I$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho đường tròn $(O; %s\\text{ cm})$ có hai dây cung $AB$ và $CD$ bằng nhau và cắt nhau tại điểm $I$ nằm bên trong đường tròn ($I \\ne O$). Gọi $H$ và $K$ lần lượt là trung điểm của $AB$ và $CD$ (minh họa như hình vẽ, với hai tia $IA, IC$ nằm cùng phía đối với đường thẳng $OI$). \\\\
a) Chứng minh rằng $OH = OK$ và đường thẳng $OI$ là đường trung trực của đoạn thẳng $HK$. \\\\
b) Chứng minh rằng $IA = IC$ và hai điểm $A, C$ đối xứng với nhau qua đường thẳng $OI$.
%s''' % (R, tikz_code))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $OA = OB = R$ và $H$ là trung điểm của $AB$ nên $OH \\perp AB$ tại $H$. Tương tự, $OK \\perp CD$ tại $K$.\\\\
Xét hai tam giác vuông $OHA$ và $OKC$ có $OA = OC = R$ và $AH = \\dfrac{AB}{2} = \\dfrac{CD}{2} = CK$, suy ra $\\Delta OHA = \\Delta OKC$ (cạnh huyền - cạnh góc vuông), do đó $OH = OK$.\\\\
Tiếp theo, xét hai tam giác vuông $OHI$ và $OKI$ có chung cạnh huyền $OI$ và $OH = OK$, suy ra $\\Delta OHI = \\Delta OKI$ (cạnh huyền - cạnh góc vuông), do đó $IH = IK$.\\\\
Vì $OH = OK$ và $IH = IK$ nên đường thẳng $OI$ là đường trung trực của đoạn thẳng $HK$.
\\item Ta có $HA = \\dfrac{AB}{2} = \\dfrac{CD}{2} = KC$ và $IH = IK$.\\\\
Do $H$ nằm giữa $I, A$ và $K$ nằm giữa $I, C$ nên $IA = IH + HA = IK + KC = IC$.\\\\
Mặt khác, từ $\\Delta OHI = \\Delta OKI$ ta có $\\widehat{HIO} = \\widehat{KIO}$, suy ra tia $IO$ là tia phân giác của $\\widehat{AIC}$.\\\\
Trong tam giác $IAC$ cân tại $I$ ($IA = IC$), đường phân giác $OI$ đồng thời là đường trung trực của cạnh đáy $AC$.\\\\
Vậy hai điểm $A$ và $C$ đối xứng với nhau qua đường thẳng $OI$.
\\end{enumEX}''')

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
