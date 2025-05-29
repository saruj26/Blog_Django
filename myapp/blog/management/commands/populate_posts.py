from blog.models import Post, Category
from django.core.management.base import BaseCommand
from typing import Any
import random


class Command(BaseCommand):
    help = "This Command inserts post data"  
  
    def handle(self, *args: Any, **options: Any):
        

        #deleting existing data
        Post.objects.all().delete()

        titles = [
    "10 Tips to Improve Your Productivity",
    "The Beginner's Guide to Python Programming",
    "How to Build a Personal Website from Scratch",
    "Understanding Artificial Intelligence in Simple Terms",
    "The Power of Daily Habits for Success",
    "Top 5 Books Every Developer Should Read",
    "How to Start a Career in Web Development",
    "Mastering Time Management: Strategies That Work",
    "Exploring the Future of Technology in 2025",
    "Why Mental Health Matters More Than Ever",
    "A Guide to Creating a Blog with Django",
    "The Pros and Cons of Remote Work",
    "Learning React: A Step-by-Step Tutorial",
    "How to Stay Motivated While Working from Home",
    "Top 10 Tools for Content Creators in 2025",
    "Design Thinking: What It Is and Why It Matters",
    "Writing Clean and Maintainable Code",
    "How to Get Started with Freelancing Online",
    "Common Mistakes New Bloggers Make",
    "The Evolution of Social Media Marketing"
]
        contents = [
    "Improving productivity starts with setting clear, achievable goals. Break tasks into smaller chunks to reduce overwhelm. Use tools like to-do lists and calendars for organization. Avoid multitasking as it reduces efficiency. Take regular breaks to recharge your focus.",
    "Python is a beginner-friendly language known for its readability. It supports multiple programming paradigms including procedural and object-oriented. Popular uses include web development, data analysis, and automation. You can write your first Python script with just a text editor and terminal. Start learning by practicing simple programs like calculators and games.",
    "Start building a website by learning HTML, CSS, and basic JavaScript. Choose a domain name and get hosting to publish your site. Use responsive design to make it mobile-friendly. Consider adding a personal portfolio or blog section. Tools like Git and VS Code will help manage your project.",
    "Artificial Intelligence mimics human intelligence through machines. It includes fields like machine learning, natural language processing, and robotics. AI is already used in everyday apps like voice assistants and recommendation engines. It learns from data to make predictions or decisions. Though powerful, ethical concerns are important when using AI.",
    "Daily habits shape our productivity and mindset. Waking up early and planning your day improves focus. Consistent exercise and healthy eating boost energy levels. Journaling and meditation reduce stress. Small daily improvements lead to long-term success.",
    "Clean Code by Robert C. Martin teaches writing readable code. You Dont Know JS series deepens JavaScript knowledge. The Pragmatic Programmer focuses on real-world software practices. Design Patterns helps understand reusable object-oriented solutions. Eloquent JavaScript is great for mastering JS fundamentals.",
    "Web development starts with learning HTML, CSS, and JavaScript. Familiarize yourself with frameworks like React or Angular. Backend development involves learning Node.js, Python, or PHP. Build projects to showcase your skills in a portfolio. Networking and internships help land your first job.",
    "Time management involves prioritizing tasks based on importance. The Pomodoro Technique encourages focus through timed work sessions. Set SMART goals to stay organized. Use tools like Trello or Notion for planning. Limit distractions like notifications and social media.",
    "By 2025, we expect major growth in AI, quantum computing, and automation. Wearables and IoT devices will be more integrated into daily life. Data privacy and cybersecurity will be top priorities. 5G and edge computing will change internet experiences. Green technology will play a bigger role in innovation.",
    "Mental health affects how we think, feel, and act. It's important to talk openly about stress, anxiety, and depression. Workplaces are adopting wellness programs to support employees. Regular exercise and mindfulness practices improve mental well-being. Seeking help should be normalized and encouraged.",
    "Django is a powerful Python web framework with built-in admin tools. Start by installing Django and creating a project. You can build blogs using models, views, and templates. Add authentication to protect your content. Use the Django admin panel to manage your blog posts.",
    "Remote work offers flexibility and better work-life balance. However, it may lead to feelings of isolation. Communication tools like Slack or Zoom are essential. It requires self-discipline and a distraction-free workspace. Employers save on infrastructure costs but must trust employees more.",
    "React is a JavaScript library for building user interfaces. Start by learning JSX, components, and props. Create your first app using Create React App. Manage state using hooks like useState and useEffect. Practice by building projects like a to-do list or calculator.",
    "Working from home requires setting a routine and clear boundaries. Keep your workspace separate from relaxation areas. Take short breaks to avoid burnout. Celebrate small wins to stay encouraged. Stay connected with peers to reduce isolation.",
    "In 2025, content creators use tools like Canva for design and Notion for planning. OBS Studio helps in streaming and recording videos. Grammarly assists with writing error-free content. AI tools like ChatGPT support idea generation. Analytics platforms like TubeBuddy optimize video performance.",
    "Design thinking is a user-centered problem-solving approach. It involves empathizing, defining problems, ideating, prototyping, and testing. It encourages creative solutions through collaboration. Businesses use it to design products that truly meet user needs. It fosters innovation and adaptability.",
    "Clean code is easy to read, understand, and maintain. Use meaningful variable names and consistent formatting. Write modular code with reusable functions. Comment code only when necessary to explain complex logic. Follow best practices and use linters to catch errors early.",
    "Freelancing starts with identifying your marketable skills. Create profiles on platforms like Upwork or Fiverr. Build a portfolio with small projects. Set clear communication and pricing expectations with clients. Deliver quality work to build a solid reputation.",
    "New bloggers often neglect SEO and keyword research. Inconsistent posting can cause readers to lose interest. Avoid copying content; originality builds credibility. Not engaging with readers reduces your blog’s impact. Track analytics to improve content over time.",
    "Social media marketing has evolved from simple posts to complex campaigns. Influencers now play a big role in brand reach. Algorithms prioritize engagement, not just reach. Video content is more engaging than static posts. Authenticity and community-building drive modern strategies."
    ]
        img_urls = [
    "https://picsum.photos/id/1/800/400",
    "https://picsum.photos/id/2/800/400",
    "https://picsum.photos/id/3/800/400",
    "https://picsum.photos/id/4/800/400",
    "https://picsum.photos/id/5/800/400",
    "https://picsum.photos/id/6/800/400",
    "https://picsum.photos/id/7/800/400",
    "https://picsum.photos/id/8/800/400",
    "https://picsum.photos/id/9/800/400",
    "https://picsum.photos/id/10/800/400",
    "https://picsum.photos/id/11/800/400",
    "https://picsum.photos/id/12/800/400",
    "https://picsum.photos/id/13/800/400",
    "https://picsum.photos/id/14/800/400",
    "https://picsum.photos/id/15/800/400",
    "https://picsum.photos/id/16/800/400",
    "https://picsum.photos/id/17/800/400",
    "https://picsum.photos/id/18/800/400",
    "https://picsum.photos/id/19/800/400",
    "https://picsum.photos/id/20/800/400"
]

        categories = Category.objects.all()

        for title,content,img_url in zip (titles,contents,img_urls):
            category = random.choice(categories)
            Post.objects.create(title = title, content = content , img_url=img_url,category = category)


        self.stdout.write(self.style.SUCCESS("Completed inserting Data"))