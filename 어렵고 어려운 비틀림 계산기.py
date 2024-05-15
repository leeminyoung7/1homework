import math

def calculate_max_inner_diameter(outer_diameter, torsion_moment, allowable_stress):
    """
    최대 안지름을 계산합니다.

    매개변수:
        outer_diameter (float): 중공축의 바깥 지름 (mm).
        torsion_moment (float): 비틀림 모멘트 (Kg-m).
        allowable_stress (float): 허용 응력 (kg/mm^2).

    반환값:
        max_inner_diameter (float): 최대 안지름 (mm).
    """
    max_inner_diameter = outer_diameter / 2  # 초기값은 바깥 지름의 반입니다.
    tol = 1e-6  # 수렴 허용 오차
    max_iterations = 1000  # 최대 반복 횟수

    for _ in range(max_iterations):
        # 바깥 지름을 이용하여 비틀림 응력을 계산합니다.
        torsion_stress = torsion_moment * max_inner_diameter / (math.pi * (outer_diameter**4 - max_inner_diameter**4) / 32)

        # 비틀림 응력이 허용 응력보다 작거나 같으면 최대 안지름을 찾은 것이므로 종료합니다.
        if torsion_stress <= allowable_stress:
            break

        # 비틀림 응력이 허용 응력보다 크면 안지름을 늘려 다시 계산합니다.
        max_inner_diameter += 0.1  # 조정 가능한 값입니다.

    return max_inner_diameter

def main():
    print("최대 안지름 계산기에 오신 것을 환영합니다!")
    print("이 프로그램은 중공축의 바깥 지름, 비틀림 모멘트, 허용 응력을 입력받아 최대 안지름을 계산합니다.")

    try:
        outer_diameter = float(input("중공축의 바깥 지름을 입력하세요 (mm): "))
        torsion_moment = float(input("비틀림 모멘트를 입력하세요 (Kg-m): "))
        allowable_stress = float(input("허용 응력을 입력하세요 (kg/mm^2): "))

        max_inner_diameter = calculate_max_inner_diameter(outer_diameter, torsion_moment, allowable_stress)
        print(f"최대 안지름은 {max_inner_diameter:.2f} mm입니다.")
    except ValueError:
        print("입력값이 잘못되었습니다. 올바른 값을 입력해주세요.")

if __name__ == "__main__":
    main()
