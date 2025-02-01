# make this a class that I import from the app.py to load the data into the vector store

class RAGData:
    def __init__(self):
        self.example_texts = [
# Insurance RAG content array
# example_texts = [
    # Customer Profile Information
    "Customer Sarah Johnson has been with our company since 2019. She prefers email communication for policy updates and holds multiple policies including auto and home insurance. Her risk profile is low, with no claims in the past 3 years.",
    "Client preferences indicate that James Martinez should be contacted during evening hours between 6-8pm EST. He has opted into our paperless billing system and uses our mobile app frequently for claims submission.",
    "The Wilson family maintains a comprehensive insurance portfolio including life, auto, and property coverage. They have expressed interest in adding flood insurance during their last annual review. Primary contact is Michael Wilson.",
    
    # Policy Management
    "Policy holders can modify their coverage through our online portal or by contacting customer service. Most common adjustments include adding drivers to auto policies and updating property values for homeowner's insurance.",
    "Premium payment preferences show that 68% of our customers opt for monthly automatic payments, while 22% prefer quarterly payments. Late payment notifications are sent 5 days before the due date.",
    
    # Claims History and Processing
    "Standard claims processing time is 5-7 business days for auto insurance and 10-14 days for property claims. Expedited processing is available for severe damage cases.",
    "Customer satisfaction data shows that clients who submit claims through our mobile app report 89% satisfaction rates, compared to 76% for phone submissions.",
    
    # Communication Preferences
    "Our analytics show that 45% of customers prefer morning calls (9am-12pm), while 35% prefer evening contact (5pm-8pm). Text message notifications have a 94% open rate.",
    "Multilingual support is available in Spanish, Mandarin, and Vietnamese. Customer language preferences are marked with a flag icon in their profile.",
    
    # Product Recommendations
    "Cross-sell opportunities should be identified based on life events: new home purchases indicate potential for bundled home/auto policies, while growing families may benefit from life insurance options.",
    "Seasonal reminders about flood insurance are sent to customers in coastal areas before hurricane season, with a 23% conversion rate.",
    
    # Customer Service Guidelines
    "First-response resolution rate target is 85%. Escalation protocols require supervisor intervention for any complaint about claim denials or premium increases.",
    "Customer feedback indicates that proactive policy reviews every 6 months lead to 34% higher retention rates and 28% more policy upgrades.",
    
    # Risk Assessment
    "Premium calculations factor in location-specific risks, with higher rates in areas prone to natural disasters. Customer risk profiles are updated quarterly based on claims history.",
    "Safe driver discounts apply after 3 years of claim-free driving, resulting in an average 15% premium reduction.",
    
    # Digital Engagement
    "Mobile app users show 45% higher retention rates and report 78% higher satisfaction scores compared to non-app users. App features include instant policy access, claims filing, and premium payments.",
    "Customers enrolled in paperless billing save an average of $12 annually on administrative fees and receive documents 2 days faster than mail delivery.",
    
    # Privacy and Security
    "Customer data access requires two-factor authentication. All policy holders must verify their identity using their policy number and last four digits of SSN.",
    "Data retention policies maintain customer records for 7 years after policy termination, with annual security audits of stored information.",
    
    # Special Programs
    "Military service members receive a 15% discount on all policies. Senior citizens over 65 qualify for additional accident forgiveness benefits.",
    "Our good student discount program offers up to 25% premium reduction for students maintaining a B average or higher."
]

# Load texts into vector store
# vector_store.add_texts(example_texts)

# Print confirmation of number of texts loaded
# print(f"Successfully loaded {len(example_texts)} text chunks into the vector store.")