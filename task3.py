def solve_contest_problem():
    # შეყვანა
    try:
        n, k = map(int, input().split())
        scores = list(map(int, input().split()))
    except:
        print("შეცდომა შეყვანისას.")
        return

    # თუ ნაკლებია ქულა, გავაგრძელოთ რაც გვაქვს
    if len(scores) < k:
        print("შეცდომა: k აღემატება მონაწილეთა რაოდენობას.")
        return

    # k-ე ადგილის ქულა
    k_th_score = scores[k - 1]

    # ვითვლით, ვინც >= k_th_score და > 0
    advancing_count = 0
    for score in scores:
        if score >= k_th_score and score > 0:
            advancing_count += 1
        else:
            break  # რადგან ქულები კლებადობითაა, დანარჩენები ვერ გადავლენ

    print(advancing_count)