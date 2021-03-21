
```bash
cd package
zip -r ../my-deployment-package.zip .
cd ..
zip -ur my-deployment-package.zip heart_rate_bot
zip -g my-deployment-package.zip lambda_function.py
```
