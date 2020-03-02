import pytest


VALID_DATA = (
    "        ID      RA (core)     DEC (core)  RA (centroid) DEC (centroid)           FLUX      Core frac           BMAJ           BMIN             PA      SIZE     CLASS SELECTION         x         y\n"
    "  19583869    -0.02718240   -29.88018036    -0.02581738   -29.88134634    3.07180e-05     0.00701535        242.875        124.447         19.617         1         1         1      16516.367      17089.901\n"
    "   2200269    -0.31122127   -29.57863808    -0.31122127   -29.57863808    3.35431e-08    -0.00000000        255.579         85.189         25.461         1         1         1      17995.551      18891.185\n"
    "  20370953    -0.15663946   -29.61390114    -0.15602246   -29.61090221    5.05104e-08     0.01313285        157.013        135.343         15.008         1         1         1      17191.154      18700.606\n"
    "   3922693    -0.56895351   -29.68047714    -0.56782715   -29.67751472    7.81801e-08     0.00048650         66.171         57.413        270.983         1         1         1      19322.199      18297.016\n"
    "  22627893    -0.10098527   -29.69201088    -0.10098527   -29.69201088    3.78579e-08    -0.00000000        346.540        180.875        310.391         1         1         1      16905.655      18217.704\n"
    "  22235175    -0.06922075   -29.68521881    -0.06820202   -29.68617504    5.47061e-08     0.09542638        165.293        143.289        246.465         1         1         1      16736.004      18252.598\n"
    "  25921337    -0.47371647   -29.72005272    -0.47610163   -29.71947938    7.71740e-08     0.00972812        245.269        135.417        280.891         1         1         1      18846.390      18049.167\n"
    "  35706997    -0.35326925   -29.51513863    -0.34831850   -29.52199813    8.44312e-07     0.00759258        402.424        168.599        239.468         1         1         1      18188.775      19228.071\n"
    "   2279500    -0.02573523   -29.84303093    -0.02573523   -29.84303093    3.39908e-08    -0.00000000        406.903        218.836        202.725         1         1         1      16515.994      17318.177\n"
    "  11334366    -0.35424319   -29.84412384    -0.35424319   -29.84412384    4.17714e-08    -0.00000000        314.448        305.980         96.737         1         1         1      18213.613      17308.851\n"
    "  19583869    -0.02718240   -29.88018036    -0.02581738   -29.88134634    3.07180e-05     0.00701535        242.875        124.447         19.617         1         1         1      16516.367      17089.901\n"
    "   2200269    -0.31122127   -29.57863808    -0.31122127   -29.57863808    3.35431e-08    -0.00000000        255.579         85.189         25.461         1         1         1      17995.551      18891.185\n"
    "  20370953    -0.15663946   -29.61390114    -0.15602246   -29.61090221    5.05104e-08     0.01313285        157.013        135.343         15.008         1         1         1      17191.154      18700.606\n"
    "   3922693    -0.56895351   -29.68047714    -0.56782715   -29.67751472    7.81801e-08     0.00048650         66.171         57.413        270.983         1         1         1      19322.199      18297.016\n"
    "  22627893    -0.10098527   -29.69201088    -0.10098527   -29.69201088    3.78579e-08    -0.00000000        346.540        180.875        310.391         1         1         1      16905.655      18217.704\n"
    "  22235175    -0.06922075   -29.68521881    -0.06820202   -29.68617504    5.47061e-08     0.09542638        165.293        143.289        246.465         1         1         1      16736.004      18252.598\n"
    "  25921337    -0.47371647   -29.72005272    -0.47610163   -29.71947938    7.71740e-08     0.00972812        245.269        135.417        280.891         1         1         1      18846.390      18049.167\n"
    "  35706997    -0.35326925   -29.51513863    -0.34831850   -29.52199813    8.44312e-07     0.00759258        402.424        168.599        239.468         1         1         1      18188.775      19228.071\n"
    "   2279500    -0.02573523   -29.84303093    -0.02573523   -29.84303093    3.39908e-08    -0.00000000        406.903        218.836        202.725         1         1         1      16515.994      17318.177\n"
    "  11334366    -0.35424319   -29.84412384    -0.35424319   -29.84412384    4.17714e-08    -0.00000000        314.448        305.980         96.737         1         1         1      18213.613      17308.851\n"
)


@pytest.fixture
def valid_text_file(tmpdir):
    """Fixture that creates a .txt file."""
    file = tmpdir.mkdir("sub").join("data.txt")
    file.write(VALID_DATA)
    return file


@pytest.fixture
def valid_csv_file(tmpdir):
    """Fixture that creates .csv file."""
    file = tmpdir.mkdir("sub").join("data.csv")
    file.write(VALID_DATA)
    return file
