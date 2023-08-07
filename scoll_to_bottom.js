    try:
        # Step 3: Define a smooth scroll function using JavaScript
        scroll_js = """
        function smoothScrollToBottom(duration) {
            const start = window.pageYOffset || document.documentElement.scrollTop;
            const end = document.body.scrollHeight - window.innerHeight;
            const startTime = performance.now();

            function scroll(timestamp) {
                const currentTime = timestamp - startTime;
                const scrollDistance = end - start;
                const easeInOutCubic = t => t<.5 ? 4*t*t*t : (t-1)*(2*t-2)*(2*t-2)+1;
                const scrollPosition = start + scrollDistance * easeInOutCubic(currentTime / duration);

                if (currentTime < duration) {
                    window.scrollTo(0, scrollPosition);
                    requestAnimationFrame(scroll);
                } else {
                    window.scrollTo(0, end);
                }
            }

            requestAnimationFrame(scroll);
        }
        """

        # Step 4: Execute the smooth scroll function with the desired duration
        duration_ms = 9000  # Change this value to set the duration of the smooth scroll in milliseconds
        duration_ms_up = -9000  # Change this value to set the duration of the smooth scroll in milliseconds
        driver.execute_script(scroll_js + f"smoothScrollToBottom({duration_ms});")
        driver.execute_script(scroll_js + f"smoothScrollToBottom({duration_ms_up});")

    except Exception as e:
        print("An error occurred:", e)
