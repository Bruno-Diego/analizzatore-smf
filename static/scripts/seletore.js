let payers = ["Martini", "Paolo Martini", "Martini Paolo", "Paolo (Martini)"]; // Add more names as needed
        let nonpayers = ["Viarizzio", "Da Silva", "Marchisio", "Morello", "Pollio", "Martini Paolo"]; // Add more names as needed
        let remainingPayers = [...payers];
        let remainingTries = payers.length; // Initialize remaining tries
        let currentIndex = 0;

        function displayRandomNonplayer() {
            if (currentIndex < nonpayers.length + 1) {
                const randomIndex = Math.floor(Math.random() * nonpayers.length);
                const selectedNonplayer = nonpayers[randomIndex];
                document.getElementById("nonplayerName").textContent = selectedNonplayer;

                // Delay for 2 seconds
                setTimeout(() => {
                    currentIndex++;
                    displayRandomNonplayer();
                }, 100);
                currentIndex = 0
            } else {
                // All names displayed, reset index or stop the loop
                // You can add additional logic here if needed
            }
        }
        function getRandomPayer() {
            if (remainingTries < payers.length) {
                document.getElementById("result").style.display = "none";
                document.getElementById("celebrate").style.display = "none";
                document.getElementById("nonplayerName").style.display = "block";
                currentIndex = 0
                displayRandomNonplayer();
            }
            displayRandomNonplayer();
            if (remainingTries > 0 && remainingPayers.length > 0) {
                const randomIndex = Math.floor(Math.random() * payers.length);
                const selectedPayer = payers[randomIndex];
                
                // Delay the result by 2 seconds
                setTimeout(() => {
                    currentIndex = nonpayers.length + 1
                    document.getElementById("result").style.display = "block";
                    document.getElementById("celebrate").style.display = "block";
                    document.getElementById("nonplayerName").style.display = "none";
                    document.getElementById("result").textContent = `Felicitazioni ${selectedPayer}!`;
                    document.getElementById("celebrate").textContent = `Sei stato scelto per pagare il prossimo giro di caffè! Buon divertimento!`;
                }, 2000); // 2000 milliseconds = 2 seconds

                remainingTries--;
            } else {
                document.getElementById("nonplayerName").style.display = "none";
                document.getElementById("result").style.display = "block";
                document.getElementById("result").textContent = "Il numero di tentativi è superato oggi, riprova domani!";
                document.getElementById("celebrate").style.display = "none";
                document.getElementsByTagName("button")[0].style.display = "none";
                document.getElementsByTagName("h5")[0].style.display = "none";
                // Optionally disable the button or provide another message
            }
        }
