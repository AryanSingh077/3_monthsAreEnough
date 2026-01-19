# # 1: grade calculator:

# a = float(input("Enter your marks in maths: "))
# b = float(input("Enter your marks in chemistry: "))
# c = float(input("Enter your marks in english: "))
# d = float(input("Enter your marks in hindi: "))
# e = float(input("Enter your marks in physics: "))

# avgMarks = float((a+b+c+d+e)/5);
# print(f"your average marks is {avgMarks}.");

# if avgMarks >= 85:
#     print("your grade is A");
# elif avgMarks >= 70:
#     print("your grade is B");
# elif avgMarks >= 55:
#     print("your grade is C");
# elif avgMarks >= 40:
#     print("Your grade is D");
# else:
#     print("Failed in examination!!");

# prob 2:Age-based eligibility checker:


# print("Benefits according to your age!!")
# age = int(input("Enter your age: "))
# gender = input("Enter your gender: ")

# if age>=60 and gender == "Male":
#     print('''-> Higher Interest Rates: Banks offer an extra 0.50%, interest on Fixed Deposits, and the SCSS (Senior Citizen Savings Scheme) provides a high government-backed rate (currently ~8.2%).

# -> Income Tax Deductions: You get a higher basic tax exemption limit (up to ₹3 lakh) and can claim up to ₹50,000 as a deduction on interest income under Section 80TTB.

# -> Healthcare Coverage: Free health insurance up to ₹5 lakh/year via Ayushman Bharat (for those 70+) and discounted medicines at Janaushadhi stores.''')

# elif age>=60 and gender == "Female":
#     print('''-> Early Concession Age: While men usually wait until 60 for many travel perks, women often qualify as senior citizens starting at age 58 (especially for Indian Railways, where they receive a higher 50%, discount compared to 40%, for men).

# -> Special Pension Schemes: Women have access to the Indira Gandhi National Widow Pension Scheme (if applicable) and general old-age pensions which often provide a slightly higher or prioritized monthly payout in several states.

# -> Health & Insurance Priority: Women over 60 get priority at government hospitals and under the Ayushman Bharat scheme, they receive a ₹5 lakh/year health cover (with age 70+ being the newest universal eligibility).''')
    
# elif age >= 18 and gender =="Male":
#     print('''-> Skill & Job Support: You can enroll in the PM Kaushal Vikas Yojana (PMKVY) for free industry-ready skill training or use the National Career Service (NCS) portal for job matching and career counseling.

# -> Startup & Business Loans: Under the Mudra Yojana, you can get collateral-free loans up to ₹10 lakh to start or expand a small business (e.g., a shop or service).

# -> Low-Cost Insurance: You can get ₹2 lakh accidental death cover for just ₹20/year via Pradhan Mantri Suraksha Bima Yojana (PMSBY) and life insurance for ₹436/year via PMJJBY.''')
    
# elif age>= 18 and gender == "Female":
#     print('''-> Entrepreneurship & Loans: You can get collateral-free business loans up to ₹10 lakh via the Mudra Yojana (often with a 0.25%, interest discount for women) or join a Self-Help Group (SHG) to access the Lakhpati Didi scheme for skill training and micro-credit.

# -> High-Interest Savings: The Mahila Samman Savings Certificate allows you to invest up to ₹2 lakh for 2 years at a fixed, high interest rate of 7.5%, which is higher than most standard bank deposits.

# -> Maternity & Health Benefits: Under PMMVY (Pradhan Mantri Matru Vandana Yojana), pregnant women receive ₹5,000 to ₹6,000 in cash transfers to support nutrition and healthcare during their first and second pregnancy.''')
    
# elif age<18 and gender == "Male":
#     print('''-> Education Scholarships: Meritorious students can access schemes like the PM Scholarship Scheme (approx. ₹2,500/month for wards of ex-servicemen) or the National Means-cum-Merit Scholarship (NMMSS), which provides ₹12,000 per year to prevent school dropouts.

# -> Government Savings Schemes: While there isn't a direct "Sukanya Samriddhi" for boys, parents can open a Public Provident Fund (PPF) or National Savings Certificate (NSC) in a minor boy's name. These offer high, tax-free returns to build a corpus for his college education.

# -> Adolescent Health Support: Under the Rashtriya Kishor Swasthya Karyakram (RKSK), boys aged 10 to 19 receive free check-ups, nutrition counseling, and iron supplements through "Adolescent Friendly Health Clinics" to ensure healthy growth.''')
    
# elif age<18 and gender == "Female":
#     print('''-> Sukanya Samriddhi Yojana (SSY): A high-interest savings account (currently 8.2%) can be opened in a girl's name before she turns 10. The investment is tax-free, and the full corpus is given to her at age 21 (or for marriage after 18) to fund her higher education or future.

# -> Merit Scholarships: For "Single Girl Children," the CBSE Merit Scholarship provides monthly financial support for Classes 11 and 12. Additionally, the Udaan Scheme provides free tablets, study materials, and coaching to help girls from various boards prepare for engineering entrance exams (JEE).

# -> Education Incentives: Under the Balika Samridhi Yojana, girls from low-income families receive cash grants upon birth and annual scholarships (from ₹300 to ₹1,000) for every year they successfully complete school up to Class 10.''')
    
# elif age<=0:
#     print("Error in input")

# else:
#     print("Error")
