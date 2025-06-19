# Local Installation to Use the Package

1. Clone the repository to your computer:
    ```bash
    git clone https://github.com/karned-kommon/shared.git
    ```
   
2. Install the requirements:
   ```bash
   cd shared
   pip install -r requirements.txt
   ```

3. Install the package in your API project:
    Navigate to your API project and activate your virtual environment, then run:

    ```bash
    pip install -e {'path of the folder in your computer'}
    ```
   
4. Configure PyCharm to recognize the package:
    Go to `Files` / `Settings` / `Project: <projectName>` / `Project Structure`

    Then click on `+ Add Content Root`, select the shared folder, and click on the folder path on the right.
    At the top, click `Mark as` and choose `Sources`.
    
    Finally, click `Apply`.
