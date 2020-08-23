from django.shortcuts import render

def getLectures():
    lectures = [
        ['Lecture 0 - Intro', '/lecture0'],
        ['Lecture 1 - The Geometry of Linear Equations', '/lecture1'],
        ['Lecture 2 - Elimination with Matrices', '/lecture2'],
        ['Lecture 3 - Multiplication and Inverse Matrices', '/lecture3'],
        ['Lecture 4 - Factorization into A = LU', '/lecture4'],
        ['Lecture 5 - Transposes, Permutations, Spaces R^n', '/lecture5'],
        ['Lecture 6 - Column Space and Nullspace', '/lecture6'],
        ['Lecture 7 - Solving Ax = 0: Pivot Variables, Special Solutions', '/lecture7'],
        ['Lecture 8 - Solving Ax = b: Row Reduced Form R', '/lecture8'],
        ['Lecture 9 - Independence, Basis, and Dimension', '/lecture9'],
        ['Lecture 10 - The Four Fundamental Subspaces', '/lecture10'],
        ['Lecture 11 - Matrix Spaces; Rank 1; Small World Graphs', '/lecture11'],
        ['Lecture 12 - Graphs, Networks, Incidence Matrices', '/lecture12'],
        ['Lecture 13 - Review 1', '/review1'],
        ['Lecture 14 - Orthogonal Vectors and Subspaces', '/lecture14'],
        ['Lecture 15 - Projections onto Subspaces', '/lecture15'],
        ['Lecture 16 - Projection Matrices and Least Squares', '/lecture16'],
        ['Lecture 17 - Orthogonal Matrices and Gram-Schmidt', '/lecture17'],
        ['Lecture 18 - Properties of Determinants', '/lecture18'],
        ['Lecture 19 - Determinant Formulas and Cofactors', '/lecture19'],
        ['Lecture 20 - Cramer\'s Rule, Inverse Matrix, and Volume', '/lecture20'],
        ['Lecture 21 - Eigenvalues and Eigenvectors', '/lecture21'],
        ['Lecture 22 - Diagonalization and Powers of A', '/lecture22'],
        ['Lecture 23 - Differential Equations and exp(At)', '/lecture23'],
        ['Lecture 24 - Markov Matrices; Fourier Series', '/lecture24'],
        ['Lecture 24b - Review 2', '/review2'],
        ['Lecture 25 - Symmetric Matrices and Positive Definiteness', '/lecture25'],
        ['Lecture 26 - Complex Matrices; Fast Fourier Transform', '/lecture26'],
        ['Lecture 27 - Positive Definite Matrices and Minima', '/lecture27'],
        ['Lecture 28 - Similar Matrices and Jordan Form', '/lecture28'],
        ['Lecture 29 - Singular Value Decomposition', '/lecture29'],
        ['Lecture 30 - Linear Transformations and Their Matrices', '/lecture30'],
        ['Lecture 31 - Change of Basis; Image Compression', '/lecture31'],
        ['Lecture 32 - Review 3', '/review3'],
        ['Lecture 33 - Left and Right Inverses; Pseudoinverse', '/lecture33'],
        ['Lecture 34 - Final Review', '/finalreview']
    ]
    return lectures

def getTitlesAndUrls():
    lectures = getLectures()
    titles = []; urls = []
    for x in range(0, len(lectures)):
        titles.append(lectures[x][0])
        urls.append(lectures[x][1])
    return titles, urls

def getContexts():
    lectures = getLectures()
    titles = getTitlesAndUrls()[0]; urls = getTitlesAndUrls()[1]
    contexts = []
    for x in range(0, len(titles)):
        if (x-1 < 0):
            contexts.append({
                'title': titles[x],
                'next': titles[x+1],
                'nextURL': urls[x+1],
                'lectures': lectures
            })
        elif (x+1 < len(titles)):
            contexts.append({
                'title': titles[x],
                'prev': titles[x-1],
                'prevURL': urls[x-1],
                'next': titles[x+1],
                'nextURL': urls[x+1],
                'lectures': lectures
            })
        else:
            contexts.append({
                'title': titles[x],
                'prev': titles[x-1],
                'prevURL': urls[x-1],
                'lectures': lectures
            })
    return contexts

contexts = getContexts()

def home(request):
    return render(request, 'laic_app/home.html', {'title': 'Home', 'lectures': getLectures()})

def lecture0(request):
    return render(request, 'laic_app/lecture0.html', contexts[0])

def lecture1(request):
    return render(request, 'laic_app/lecture1.html', contexts[1])

def lecture2(request):
    return render(request, 'laic_app/lecture2.html', contexts[2])

def lecture3(request):
    return render(request, 'laic_app/lecture3.html', contexts[3])

def lecture4(request):
    return render(request, 'laic_app/lecture4.html', contexts[4])

def lecture5(request):
    return render(request, 'laic_app/lecture5.html', contexts[5])

def lecture6(request):
    return render(request, 'laic_app/lecture6.html', contexts[6])

def lecture7(request):
    return render(request, 'laic_app/lecture7.html', contexts[7])

def lecture8(request):
    return render(request, 'laic_app/lecture8.html', contexts[8])

def lecture9(request):
    return render(request, 'laic_app/lecture9.html', contexts[9])

def lecture10(request):
    return render(request, 'laic_app/lecture10.html', contexts[10])

def lecture11(request):
    return render(request, 'laic_app/lecture11.html', contexts[11])

def lecture12(request):
    return render(request, 'laic_app/lecture12.html', contexts[12])

def review1(request):
    return render(request, 'laic_app/review1.html', contexts[13])

def lecture14(request):
    return render(request, 'laic_app/lecture14.html', contexts[14])

def lecture15(request):
    return render(request, 'laic_app/lecture15.html', contexts[15])

def lecture16(request):
    return render(request, 'laic_app/lecture16.html', contexts[16])

def lecture17(request):
    return render(request, 'laic_app/lecture17.html', contexts[17])

def lecture18(request):
    return render(request, 'laic_app/lecture18.html', contexts[18])

def lecture19(request):
    return render(request, 'laic_app/lecture19.html', contexts[19])

def lecture20(request):
    return render(request, 'laic_app/lecture20.html', contexts[20])

def lecture21(request):
    return render(request, 'laic_app/lecture21.html', contexts[21])

def lecture22(request):
    return render(request, 'laic_app/lecture22.html', contexts[22])

def lecture23(request):
    return render(request, 'laic_app/lecture23.html', contexts[23])

def lecture24(request):
    return render(request, 'laic_app/lecture24.html', contexts[24])

def review2(request):
    return render(request, 'laic_app/review2.html', contexts[25])

def lecture25(request):
    return render(request, 'laic_app/lecture25.html', contexts[26])

def lecture26(request):
    return render(request, 'laic_app/lecture26.html', contexts[27])

def lecture27(request):
    return render(request, 'laic_app/lecture27.html', contexts[28])

def lecture28(request):
    return render(request, 'laic_app/lecture28.html', contexts[29])

def lecture29(request):
    return render(request, 'laic_app/lecture29.html', contexts[30])

def lecture30(request):
    return render(request, 'laic_app/lecture30.html', contexts[31])

def lecture31(request):
    return render(request, 'laic_app/lecture31.html', contexts[32])

def review3(request):
    return render(request, 'laic_app/review3.html', contexts[33])

def lecture33(request):
    return render(request, 'laic_app/lecture33.html', contexts[34])

def finalreview(request):
    return render(request, 'laic_app/finalreview.html', contexts[35])