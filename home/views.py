from django.shortcuts import redirect, render
from selenium import webdriver
from selenium import webdriver
from home.models import Job, Category

# browser --> chrome
def job():
    print('runing the function')
    # url for categories of jobs
    driver = webdriver.Chrome('C:\\Users\\jayesh kaushik\\Documents\\persnal projects\\mini projects\\web scraping\\chromedriver.exe')
    category = 'https://www.careerguide.com/career-options'
    driver.get(category)

    # fetching data using classname
    jobTitles = driver.find_elements_by_class_name('col-md-4')
    JobNameUrlArr = []
    JobDetailsArr = []
    for jobTitle in jobTitles:
        try:
            subCategory = ''
            category = jobTitle.find_element_by_class_name('c-font-bold').text
            subCategories = jobTitle.find_elements_by_class_name(
                'c-content-list-1')

            for subCate in subCategories:
                subCategory = subCate.text.split('\n')
            JobDetails = {'category': category, 'subCategory': subCategory}
            JobDetailsArr.append(JobDetails)

            # saving category of job to database
            ModelCategory = Category(job_category=category, job_subcategory=str(subCategory))
            ModelCategory.save()

            JobNameList = category.lower().split(' ')
            JobNameUrl = ''
            for i in range(len(JobNameList)):
                if JobNameList[i] == '/':
                    JobNameUrl += '+'
                elif JobNameList[i] == '&':
                    JobNameUrl += '+'
                else:
                    JobNameUrl += JobNameList[i]
            JobNameUrlArr.append(JobNameUrl)

        except Exception as e:
            continue

    # fetching the data from the linkedIn using the JobNameUrl and linkedIn url
    for i in range(0, len(JobNameUrlArr), 5):

        url = JobNameUrlArr[i]
        linkedInUrl = f'https://www.linkedin.com/jobs/search/?keywords={url}&position=1&pageNum=0'
        print(linkedInUrl)
        driver.get(linkedInUrl)

        # scraping data using class name
        info = driver.find_elements_by_class_name('base-search-card__info')
        for post in info:
            # fetching job title name
            jobtitle = post.find_element_by_class_name(
                'base-search-card__title').text
            # fetchin company name
            company = post.find_element_by_class_name(
                'base-search-card__subtitle').text
            # location of company
            location = post.find_element_by_class_name(
                'job-search-card__location').text

            # saving the job details to the database
            job = Job(company=company, job_position=jobtitle, location=location)
            job.save()

    return redirect('/')



def index(request):
    jobs = Job.objects.all()
    return render(request, 'index.html', {'jobs':jobs})