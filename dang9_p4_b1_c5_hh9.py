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


def bt_dang9_p4_b1_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.randint(1, 4)
        nua_canh = 3 * k
        canh = 6 * k
        ag_coef = 2 * k

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (B) at (-1.5,0);
\\coordinate (C) at (1.5,0);
\\coordinate (H) at (0,0);
\\coordinate (A) at (0,2.598);
\\coordinate (G) at (0,0.866);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (A)--(H);
\\draw[line width=1pt] (0,0.2)--(0.2,0.2)--(0.2,0);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (H) circle (1pt) node[below] {$H$};
\\fill (G) circle (1pt) node[right] {$G$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho tam giác đều $ABC$ cạnh $%s\\text{ cm}$, có đường cao $AH$ và trọng tâm $G$ (như hình vẽ). Xét đường tròn $(A; %s\\sqrt{3}\\text{ cm})$. \\\\
a) Trong bốn điểm $B, C, H, G$, điểm nào nằm trên, điểm nào nằm trong và điểm nào nằm ngoài đường tròn $(A; %s\\sqrt{3}\\text{ cm})$? Vì sao? \\\\
b) Chứng minh rằng đường thẳng $AH$ là trục đối xứng của cả tam giác $ABC$ và đường tròn $(A; %s\\sqrt{3}\\text{ cm})$.
%s''' % (canh, nua_canh, nua_canh, nua_canh, tikz_code))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Bán kính của đường tròn là $R = %s\\sqrt{3} = \\sqrt{%s}\\text{ cm}$.\\\\
- Ta có $AB = AC = %s = \\sqrt{%s}\\text{ cm}$. Vì $AB = AC > R$ nên hai điểm $B$ và $C$ nằm ngoài đường tròn $(A; %s\\sqrt{3}\\text{ cm})$.\\\\
- Vì tam giác $ABC$ đều nên đường cao $AH$ đồng thời là đường trung tuyến, suy ra $BH = \\dfrac{BC}{2} = %s\\text{ cm}$. Áp dụng định lí Pythagore cho tam giác $ABH$ vuông tại $H$, ta có:\\\\
$AH = \\sqrt{AB^2 - BH^2} = \\sqrt{%s^2 - %s^2} = %s\\sqrt{3}\\text{ cm} = R$. Do đó điểm $H$ nằm trên đường tròn $(A; %s\\sqrt{3}\\text{ cm})$.\\\\
- Vì $G$ là trọng tâm tam giác $ABC$ nên $AG = \\dfrac{2}{3}AH = %s\\sqrt{3}\\text{ cm} < %s\\sqrt{3}\\text{ cm} = R$. Do đó điểm $G$ nằm trong đường tròn $(A; %s\\sqrt{3}\\text{ cm})$.
\\item Trong tam giác đều $ABC$, đường cao $AH$ cũng là đường trung trực của đoạn thẳng $BC$, nên hai điểm $B$ và $C$ đối xứng với nhau qua $AH$, tức là $AH$ là trục đối xứng của tam giác $ABC$.\\\\
Mặt khác, đường thẳng $AH$ đi qua tâm $A$ của đường tròn $(A; %s\\sqrt{3}\\text{ cm})$ nên $AH$ cũng là một trục đối xứng của đường tròn này.
\\end{enumEX}''' % (nua_canh, 3*(nua_canh**2), canh, canh**2, nua_canh, nua_canh, canh, nua_canh, nua_canh, nua_canh, ag_coef, nua_canh, nua_canh, nua_canh))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
