INTERVIEW_QUESTIONS = {
    "Data Science": [
        {
            "question": "Tell me about yourself and your data science experience",
            "expected": "background education skills projects experience data science machine learning python"
        },
        {
            "question": "Explain the difference between supervised and unsupervised learning",
            "expected": "supervised learning uses labeled data with input output pairs unsupervised learning finds patterns in unlabeled data without predefined outputs clustering classification regression"
        },
        {
            "question": "What is overfitting and how do you prevent it?",
            "expected": "overfitting happens when model memorizes training data performs poorly on new unseen data prevent using regularization cross validation more training data dropout early stopping"
        },
        {
            "question": "Explain how a Random Forest algorithm works",
            "expected": "random forest is ensemble method combines multiple decision trees bagging technique reduces overfitting averages predictions improves accuracy"
        },
        {
            "question": "What is the difference between correlation and causation?",
            "expected": "correlation means two variables move together statistical relationship causation means one variable directly causes change in another correlation does not imply causation"
        },
        {
            "question": "How do you handle missing data in a dataset?",
            "expected": "handle missing data using imputation mean median mode removing rows or columns forward fill backward fill predictive imputation depending on data type and amount missing"
        },
        {
            "question": "Explain the bias-variance tradeoff",
            "expected": "bias error from wrong assumptions underfitting variance error from sensitivity to training data overfitting tradeoff balance between simple and complex models for better generalization"
        },
        {
            "question": "What evaluation metrics do you use for classification problems?",
            "expected": "accuracy precision recall f1 score confusion matrix roc auc curve depending on class balance and business requirement"
        },
        {
            "question": "How would you explain a machine learning model to a non-technical person?",
            "expected": "use simple analogy explain pattern recognition learning from examples making predictions avoid jargon focus on business value and outcomes"
        },
        {
            "question": "Describe a data science project you have worked on",
            "expected": "problem statement data collection cleaning preprocessing model building evaluation results impact deployment tools used python pandas sklearn"
        },
        {
            "question": "What is cross-validation and why is it important?",
            "expected": "cross validation splits data into multiple folds trains and tests model on different combinations gives reliable estimate of model performance prevents overfitting k fold"
        },
        {
            "question": "How do you handle imbalanced datasets?",
            "expected": "handle imbalanced data using oversampling undersampling smote class weights different evaluation metrics like f1 score precision recall instead of accuracy"
        }
    ],

    "Full Stack Developer": [
        {
            "question": "Tell me about yourself and your development experience",
            "expected": "background education skills projects experience frontend backend full stack development languages frameworks"
        },
        {
            "question": "Explain the difference between REST API and GraphQL",
            "expected": "rest api uses multiple endpoints fixed data structure graphql uses single endpoint flexible queries client requests exactly needed data reduces over fetching"
        },
        {
            "question": "What is the difference between SQL and NoSQL databases?",
            "expected": "sql databases relational structured schema tables rows nosql databases non relational flexible schema documents key value pairs better for unstructured data scalability"
        },
        {
            "question": "How does authentication and authorization work in web apps?",
            "expected": "authentication verifies user identity login credentials tokens jwt authorization determines what permissions access rights user has after authentication"
        },
        {
            "question": "Explain how React state management works",
            "expected": "state holds component data useState hook manages local state context api redux for global state changes trigger re render of components"
        },
        {
            "question": "What is the difference between GET and POST requests?",
            "expected": "get request retrieves data parameters in url no body idempotent post request sends data in body creates or updates resources not idempotent"
        },
        {
            "question": "How do you optimize a slow web application?",
            "expected": "optimize using caching lazy loading code splitting minimizing bundle size database indexing query optimization cdn compressing images reducing http requests"
        },
        {
            "question": "Explain how you would design a scalable backend system",
            "expected": "scalable backend uses load balancing horizontal scaling microservices caching database sharding message queues stateless servers"
        },
        {
            "question": "What is Docker and why is it useful?",
            "expected": "docker is containerization platform packages application with dependencies ensures consistency across environments easier deployment scaling isolation"
        },
        {
            "question": "How do you handle errors in a Node.js application?",
            "expected": "handle errors using try catch blocks error handling middleware promise rejection handlers logging errors proper http status codes"
        },
        {
            "question": "Explain the concept of microservices",
            "expected": "microservices architecture breaks application into small independent services each with own database communicate via apis easier to scale and deploy independently"
        },
        {
            "question": "What is CI/CD and how have you used it?",
            "expected": "ci continuous integration automatically testing code changes cd continuous deployment automatically deploying to production using tools like github actions jenkins pipeline automation"
        }
    ],

    "Data Analyst": [
        {
            "question": "Tell me about yourself and your analytics experience",
            "expected": "background education skills projects experience data analysis sql excel visualization tools reporting"
        },
        {
            "question": "How do you approach a new data analysis problem?",
            "expected": "understand business question collect relevant data clean and explore data analyze patterns trends create visualizations draw conclusions present insights"
        },
        {
            "question": "What SQL queries do you use most frequently?",
            "expected": "select where group by having join order by aggregate functions sum count average subqueries window functions"
        },
        {
            "question": "Explain the difference between INNER JOIN and LEFT JOIN",
            "expected": "inner join returns only matching rows from both tables left join returns all rows from left table and matching rows from right table with nulls if no match"
        },
        {
            "question": "How do you create effective data visualizations?",
            "expected": "choose right chart type for data clear labels titles avoid clutter use colors meaningfully highlight key insights tell a story with data"
        },
        {
            "question": "What tools do you use for data analysis?",
            "expected": "excel sql python pandas tableau power bi google sheets jupyter notebook for analysis and visualization"
        },
        {
            "question": "How do you identify trends in data?",
            "expected": "use time series analysis moving averages comparing periods visualizing data over time identifying patterns seasonality outliers"
        },
        {
            "question": "Explain a time you found a key insight from data",
            "expected": "describe specific project analyzed data found unexpected pattern or trend communicated insight to stakeholders resulted in business action or decision"
        },
        {
            "question": "How do you handle dirty or inconsistent data?",
            "expected": "identify missing values duplicates inconsistent formats standardize data remove or impute missing values validate data types document cleaning steps"
        },
        {
            "question": "What is A/B testing and how does it work?",
            "expected": "ab testing compares two versions of something randomly assign users to groups measure metric difference statistical significance to determine which performs better"
        },
        {
            "question": "How do you present data findings to stakeholders?",
            "expected": "simplify technical details focus on business impact use clear visualizations storytelling tailor message to audience provide actionable recommendations"
        },
        {
            "question": "What is the difference between mean, median, and mode?",
            "expected": "mean is average of all values median is middle value when sorted mode is most frequently occurring value each useful for different data distributions"
        }
    ],

    "ML Engineer": [
        {
            "question": "Tell me about yourself and your ML engineering experience",
            "expected": "background education skills projects experience machine learning deployment production model building"
        },
        {
            "question": "How do you deploy a machine learning model to production?",
            "expected": "package model using docker create api with flask or fastapi deploy on cloud platform set up monitoring and logging version the model"
        },
        {
            "question": "Explain the difference between batch and real-time inference",
            "expected": "batch inference processes large amounts of data periodically scheduled real time inference processes individual requests immediately low latency required"
        },
        {
            "question": "What is model drift and how do you monitor it?",
            "expected": "model drift occurs when model performance degrades over time due to changing data patterns monitor using performance metrics data distribution comparisons alerts"
        },
        {
            "question": "How do you optimize model performance for production?",
            "expected": "optimize using model quantization pruning distillation caching batching requests using efficient frameworks like onnx tensorrt"
        },
        {
            "question": "Explain how you would build an NLP pipeline",
            "expected": "text preprocessing tokenization cleaning feature extraction embeddings model selection training evaluation deployment using libraries like huggingface spacy"
        },
        {
            "question": "What is transfer learning and when do you use it?",
            "expected": "transfer learning uses pretrained model on new task fine tuning saves training time and data useful when limited labeled data available"
        },
        {
            "question": "How do you handle large datasets that don't fit in memory?",
            "expected": "use data generators batch processing distributed computing frameworks like spark dask chunking data reading in batches"
        },
        {
            "question": "Explain the difference between BERT and GPT models",
            "expected": "bert is bidirectional encoder understands context from both directions good for classification gpt is unidirectional decoder generates text autoregressive good for generation tasks"
        },
        {
            "question": "How do you version control ML models?",
            "expected": "use tools like mlflow dvc git lfs track model versions parameters metrics datasets reproducibility experiment tracking"
        },
        {
            "question": "What is feature engineering and why is it important?",
            "expected": "feature engineering creates new input variables from raw data improves model performance includes scaling encoding creating interaction features domain knowledge"
        },
        {
            "question": "How do you reduce model inference time?",
            "expected": "reduce inference time using model quantization pruning smaller architectures hardware acceleration gpu caching batch predictions"
        }
    ],

    "Frontend Developer": [
        {
            "question": "Tell me about yourself and your frontend experience",
            "expected": "background education skills projects experience html css javascript react frontend frameworks"
        },
        {
            "question": "Explain the difference between CSS Flexbox and Grid",
            "expected": "flexbox is one dimensional layout for rows or columns grid is two dimensional layout for rows and columns together flexbox good for components grid good for page layouts"
        },
        {
            "question": "What is the Virtual DOM in React?",
            "expected": "virtual dom is lightweight copy of actual dom react updates virtual dom first compares with previous version and updates only changed parts in real dom improves performance"
        },
        {
            "question": "How do you optimize website performance?",
            "expected": "optimize using lazy loading code splitting image compression minifying css js using cdn caching reducing render blocking resources"
        },
        {
            "question": "Explain the difference between let, var, and const in JavaScript",
            "expected": "var is function scoped can be redeclared let is block scoped can be reassigned const is block scoped cannot be reassigned all affect variable declaration and scope"
        },
        {
            "question": "What is responsive design and how do you implement it?",
            "expected": "responsive design adapts layout to different screen sizes implement using media queries flexible grids relative units like percentages and rem mobile first approach"
        },
        {
            "question": "How do you handle cross-browser compatibility issues?",
            "expected": "test on multiple browsers use css prefixes polyfills feature detection avoid browser specific features use frameworks that handle compatibility"
        },
        {
            "question": "Explain how JavaScript promises work",
            "expected": "promises represent eventual completion of asynchronous operation has states pending fulfilled rejected use then catch for handling results async await is syntactic sugar over promises"
        },
        {
            "question": "What is the difference between == and === in JavaScript?",
            "expected": "double equals compares values with type coercion triple equals compares values and types strictly without conversion triple equals is recommended for accuracy"
        },
        {
            "question": "How do you manage state in a React application?",
            "expected": "manage state using useState for local state context api or redux for global state lifting state up for shared state between components"
        },
        {
            "question": "What is lazy loading and why is it useful?",
            "expected": "lazy loading delays loading of resources until needed reduces initial page load time improves performance especially for images and components not immediately visible"
        },
        {
            "question": "How do you ensure web accessibility in your projects?",
            "expected": "use semantic html alt text for images proper color contrast keyboard navigation aria labels test with screen readers follow wcag guidelines"
        }
    ],

    "Backend Developer": [
        {
            "question": "Tell me about yourself and your backend experience",
            "expected": "background education skills projects experience backend development databases apis server side languages"
        },
        {
            "question": "How do you design a RESTful API?",
            "expected": "use proper http methods get post put delete meaningful resource based urls status codes versioning consistent response format documentation"
        },
        {
            "question": "Explain the difference between SQL and NoSQL databases",
            "expected": "sql databases relational structured schema tables nosql databases non relational flexible schema documents better for unstructured data and horizontal scaling"
        },
        {
            "question": "How do you handle authentication in a backend system?",
            "expected": "use jwt tokens session based authentication oauth password hashing with bcrypt secure storage of credentials refresh tokens"
        },
        {
            "question": "What is caching and how does it improve performance?",
            "expected": "caching stores frequently accessed data in fast storage like redis memcached reduces database load improves response time"
        },
        {
            "question": "How do you prevent SQL injection attacks?",
            "expected": "use parameterized queries prepared statements orm input validation sanitization avoid string concatenation in queries"
        },
        {
            "question": "Explain how you would design a database schema",
            "expected": "identify entities relationships normalize tables define primary foreign keys consider indexing for performance plan for scalability"
        },
        {
            "question": "What is the difference between synchronous and asynchronous code?",
            "expected": "synchronous code executes sequentially blocking asynchronous code executes non blocking allows other operations to continue using callbacks promises async await"
        },
        {
            "question": "How do you handle API rate limiting?",
            "expected": "implement rate limiting using token bucket or sliding window algorithm return 429 status code when limit exceeded use middleware or api gateway"
        },
        {
            "question": "Explain how message queues work",
            "expected": "message queues allow asynchronous communication between services producer sends messages consumer processes them decouples services improves scalability examples rabbitmq kafka"
        },
        {
            "question": "What is load balancing and why is it important?",
            "expected": "load balancing distributes incoming traffic across multiple servers improves availability prevents overload ensures reliability and scalability"
        },
        {
            "question": "How do you monitor and debug a production server?",
            "expected": "use logging tools monitoring dashboards like grafana prometheus error tracking tools alerts for anomalies analyzing logs for debugging issues"
        }
    ],

    "DevOps Engineer": [
        {
            "question": "Tell me about yourself and your DevOps experience",
            "expected": "background education skills projects experience devops ci cd cloud infrastructure automation"
        },
        {
            "question": "Explain the difference between Docker and Kubernetes",
            "expected": "docker is containerization tool packages applications kubernetes is orchestration platform manages multiple containers across clusters handles scaling deployment networking"
        },
        {
            "question": "What is CI/CD and how have you implemented it?",
            "expected": "ci continuous integration automatically builds and tests code cd continuous deployment automatically deploys to environments using tools like jenkins github actions gitlab ci pipelines"
        },
        {
            "question": "How do you monitor application performance in production?",
            "expected": "use monitoring tools like prometheus grafana datadog track metrics like cpu memory response time set up alerts for anomalies log aggregation"
        },
        {
            "question": "Explain how you would set up a deployment pipeline",
            "expected": "code commit triggers build run tests build artifact deploy to staging run integration tests deploy to production with rollback strategy"
        },
        {
            "question": "What is Infrastructure as Code and what tools do you use?",
            "expected": "infrastructure as code manages infrastructure through code files instead of manual configuration tools like terraform ansible cloudformation enables version control and reproducibility"
        },
        {
            "question": "How do you handle zero-downtime deployments?",
            "expected": "use blue green deployment rolling updates canary deployments load balancer to redirect traffic ensure backward compatibility during transitions"
        },
        {
            "question": "Explain the difference between horizontal and vertical scaling",
            "expected": "horizontal scaling adds more machines or instances vertical scaling increases resources of existing machine horizontal scaling better for distributed systems and high availability"
        },
        {
            "question": "What is a reverse proxy and why is it used?",
            "expected": "reverse proxy sits in front of servers forwards client requests provides load balancing ssl termination caching security examples nginx apache"
        },
        {
            "question": "How do you handle security in a DevOps environment?",
            "expected": "implement secrets management least privilege access scanning for vulnerabilities in code and containers network security policies regular security audits"
        },
        {
            "question": "What cloud platforms have you worked with?",
            "expected": "aws azure google cloud platform services like ec2 s3 lambda compute storage networking databases for cloud platforms"
        },
        {
            "question": "How do you manage secrets and environment variables securely?",
            "expected": "use secret management tools like vault aws secrets manager environment variables not hardcoded in code encrypted storage access control for sensitive data"
        }
    ],

    "Cybersecurity Analyst": [
        {
            "question": "Tell me about yourself and your cybersecurity experience",
            "expected": "background education skills projects experience cybersecurity network security threat analysis"
        },
        {
            "question": "What is the difference between symmetric and asymmetric encryption?",
            "expected": "symmetric encryption uses same key for encryption and decryption faster asymmetric encryption uses public and private key pairs more secure for key exchange used in different scenarios"
        },
        {
            "question": "Explain how a man-in-the-middle attack works",
            "expected": "attacker intercepts communication between two parties without their knowledge can eavesdrop or alter messages prevented using encryption ssl tls certificates"
        },
        {
            "question": "What is penetration testing and how do you approach it?",
            "expected": "penetration testing simulates attacks to find vulnerabilities approach includes reconnaissance scanning exploitation reporting remediation recommendations with proper authorization"
        },
        {
            "question": "How do you respond to a security incident?",
            "expected": "identify and contain the incident assess impact eradicate threat recover systems document findings conduct post incident review to prevent future occurrences"
        },
        {
            "question": "What is the CIA triad in cybersecurity?",
            "expected": "confidentiality ensures data is accessible only to authorized users integrity ensures data is accurate and unaltered availability ensures systems and data are accessible when needed"
        },
        {
            "question": "Explain how SQL injection attacks work and how to prevent them",
            "expected": "sql injection inserts malicious sql code through input fields to manipulate database prevent using parameterized queries input validation prepared statements"
        },
        {
            "question": "What is a firewall and how does it protect a network?",
            "expected": "firewall monitors and controls incoming and outgoing network traffic based on security rules blocks unauthorized access acts as barrier between trusted and untrusted networks"
        },
        {
            "question": "How do you perform a vulnerability assessment?",
            "expected": "scan systems using automated tools identify weaknesses prioritize based on severity verify findings provide remediation recommendations document results"
        },
        {
            "question": "What is social engineering and how do you defend against it?",
            "expected": "social engineering manipulates people into revealing confidential information defend using security awareness training verification procedures multi factor authentication"
        },
        {
            "question": "Explain the difference between IDS and IPS",
            "expected": "ids intrusion detection system monitors and alerts on suspicious activity ips intrusion prevention system actively blocks detected threats both used for network security"
        },
        {
            "question": "How do you stay updated with the latest security threats?",
            "expected": "follow security blogs news sources subscribe to vulnerability databases attend webinars conferences participate in security communities continuous learning certifications"
        }
    ],

    "Business Analyst": [
        {
            "question": "Tell me about yourself and your business analysis experience",
            "expected": "background education skills projects experience business analysis requirements gathering stakeholder management"
        },
        {
            "question": "How do you gather requirements from stakeholders?",
            "expected": "conduct interviews workshops surveys observation document analysis prototyping to understand stakeholder needs and expectations"
        },
        {
            "question": "Explain the difference between functional and non-functional requirements",
            "expected": "functional requirements describe what system should do specific features behaviors non functional requirements describe how system performs quality attributes like performance security usability"
        },
        {
            "question": "What is Agile methodology and how have you used it?",
            "expected": "agile is iterative development approach with sprints frequent feedback collaboration used in writing user stories participating in standups sprint planning reviews retrospectives"
        },
        {
            "question": "How do you handle conflicting requirements from different stakeholders?",
            "expected": "facilitate discussions prioritize based on business value impact find common ground negotiate compromises escalate to decision makers when needed document agreed decisions"
        },
        {
            "question": "What tools do you use for process mapping?",
            "expected": "use tools like visio lucidchart bizagi draw io to create flowcharts process diagrams swimlane diagrams for visualizing business processes"
        },
        {
            "question": "How do you measure the success of a project?",
            "expected": "define key performance indicators measure against project objectives track metrics like roi user adoption time savings cost reduction stakeholder satisfaction"
        },
        {
            "question": "Explain how you would conduct a gap analysis",
            "expected": "identify current state document desired future state compare to find gaps analyze root causes recommend solutions to bridge gaps"
        },
        {
            "question": "What is a use case and how do you write one?",
            "expected": "use case describes interaction between user and system to achieve goal includes actors preconditions main flow alternative flows postconditions"
        },
        {
            "question": "How do you prioritize requirements?",
            "expected": "use techniques like moscow method must should could wont have value versus effort matrix stakeholder input business priorities to rank requirements"
        },
        {
            "question": "Explain how you would create a business requirements document",
            "expected": "include project overview objectives scope stakeholders functional and non functional requirements assumptions constraints approval process"
        },
        {
            "question": "How do you handle scope creep in a project?",
            "expected": "establish clear scope baseline implement change control process evaluate impact of changes communicate with stakeholders document approved changes"
        }
    ],

    "Product Manager": [
        {
            "question": "Tell me about yourself and your product management experience",
            "expected": "background education skills projects experience product management roadmap strategy stakeholder collaboration"
        },
        {
            "question": "How do you define a product roadmap?",
            "expected": "align roadmap with company vision and goals prioritize features based on customer value and business impact include timelines milestones communicate with stakeholders"
        },
        {
            "question": "Explain how you prioritize features for a product",
            "expected": "use frameworks like rice score value versus effort moscow method consider customer feedback business goals technical feasibility"
        },
        {
            "question": "What metrics do you use to measure product success?",
            "expected": "use metrics like user engagement retention rate conversion rate revenue customer satisfaction nps depending on product goals"
        },
        {
            "question": "How do you gather and incorporate user feedback?",
            "expected": "collect feedback through surveys interviews user testing analytics review feedback regularly prioritize based on impact incorporate into roadmap"
        },
        {
            "question": "Explain the difference between product vision and product strategy",
            "expected": "product vision is long term aspirational goal for the product product strategy is the plan and approach to achieve that vision including target market positioning"
        },
        {
            "question": "How do you work with engineering and design teams?",
            "expected": "collaborate through regular communication sprint planning clear requirements documentation feedback loops resolving blockers ensuring alignment on priorities"
        },
        {
            "question": "What is an MVP and how do you define one?",
            "expected": "mvp minimum viable product is simplest version of product with core features to test with users define by identifying essential features that solve main problem"
        },
        {
            "question": "How do you handle stakeholder expectations?",
            "expected": "communicate transparently set realistic timelines manage expectations through regular updates align on priorities address concerns proactively"
        },
        {
            "question": "Explain how you would launch a new product feature",
            "expected": "plan launch strategy coordinate with marketing sales support teams prepare documentation communication monitor metrics post launch gather feedback iterate"
        },
        {
            "question": "How do you make data-driven product decisions?",
            "expected": "analyze user data analytics conduct ab testing gather qualitative feedback combine quantitative and qualitative insights to make informed decisions"
        },
        {
            "question": "What frameworks do you use for product prioritization?",
            "expected": "use frameworks like rice reach impact confidence effort moscow method kano model value versus effort matrix to prioritize features"
        }
    ]
}

DURATION_QUESTIONS = {
    "30 mins": 5,
    "45 mins": 8,
    "1 hour": 12
}

JOB_ROLES = list(INTERVIEW_QUESTIONS.keys())