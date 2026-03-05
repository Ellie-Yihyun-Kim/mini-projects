import matplotlib.pyplot as plt
import pandas as pd

# 1. 가상의 세포 좌표와 발현량 데이터 생성 (Generating synthetic cell coordinates and expression data)
data = {
    'x': [1, 2, 3, 8, 9, 10],
    'y': [1, 2, 1, 8, 9, 8],
    # 앞쪽은 암세포, 뒤쪽은 정상세포 가정( Note: First 3 points represent cancer cells; remaining 3 represents normal cells) 
    'gene_expression': [100, 95, 110, 10, 5, 15]    
}
# Dictionary를 표(Table) 형태인 DataFrame으로 변환하는 함수; DataFrame(df): 엑셀 시트와 유사함; x, y: 세포의 위치(Spatial coordinates), gene_expression: 해당 위치에서의 유전자 발현량(Expression intensity)
df = pd.DataFrame(data)

# 2. 시각화(어디에 어떤 세포가 모여있는지 확인) (Visualize the spatial distribution of cells)
# 1) Scatter plot 그리기
## df['x'], df['y']: 데이터프레임에서 x좌표와 y좌표 열을 가져와 점을 찍는다.
## c=df['gene_expression']: c는 Color의 약자. 발현량 수치에 따라 점의 색깔을 다르게 칠하라는 뜻. (예: 암세포는 높은 수치니까 밝은색, 정상은 낮은 수치니까 어두운색)
## cmap='viridis': Color Map의 약자로, 색상 테마. 'viridis'는 생물정보학 논문에서 가장 선호하는 테마 중 하나로, 색맹인 사람도 구분하기 쉽고 수치 변화가 직관적.
plt.figure(figsize=(6,5))

plt.scatter(df['x'], df['y'], c=df['gene_expression'], cmap='viridis')
# 2) Colorbar 추가
## 우측에 막대기 모양의 범례를 추가. "어떤 색이 몇 점인지"를 보여줌. 산업계 보고서나 논문에서 이 컬러바가 없으면 "데이터 해석이 불가능하다"는 지적을 받기 쉬움.
plt.colorbar(label='Gene Expression Level')
# 3) 제목과 실행
## plt.title: 그래프 상단에 제목을 단다.
plt.title("Spatial Cell Map")
## plt.show(): 메모리에 그려진 그래프를 화면에 실제로 띄운다.
plt.savefig("../outputs/spatial_cell_map.png", dpi=200, bbox_inches="tight")
plt.show()
