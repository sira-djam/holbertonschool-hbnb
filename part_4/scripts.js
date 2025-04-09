document.addEventListener("DOMContentLoaded", function() {
  // Données des lieux avec leurs prix
  const places = [
      { name: "Paris", price: 100 },
      { name: "New York", price: 200 },
      { name: "Tokyo", price: 150 },
      { name: "Londres", price: 180 },
      { name: "Berlin", price: 120 }
  ];

  // Données des prix pour le filtre
  const prices = [50, 100, 150, 200];

  // Remplir la liste déroulante avec les options de prix
  const priceFilter = document.getElementById("price-filter");

  prices.forEach(price => {
      const option = document.createElement("option");
      option.value = price;
      option.textContent = `${price}€`;
      priceFilter.appendChild(option);
  });

  // Fonction pour afficher les lieux filtrés sous forme de cartes
  function displayPlaces(maxPrice) {
      const placesList = document.getElementById("places-list");
      placesList.innerHTML = ""; // Réinitialise la liste avant d'ajouter de nouveaux éléments

      const filteredPlaces = places.filter(place => place.price <= maxPrice);

      filteredPlaces.forEach(place => {
          // Créer la carte pour chaque lieu
          const card = document.createElement("div");
          card.classList.add("place-card");

          card.innerHTML = `
              <h3>${place.name}</h3>
              <p>Prix par nuit: ${place.price}€</p>
              <button class="details-button">View Details</button>
          `;

          // Ajouter la carte à la liste
          placesList.appendChild(card);
      });
  }

  // Afficher tous les lieux au début
  displayPlaces(200);

  // Ajouter un écouteur d'événements pour filtrer en fonction du prix
  priceFilter.addEventListener("change", function() {
      const selectedPrice = parseInt(priceFilter.value);
      displayPlaces(selectedPrice);
  });
});

document.addEventListener("DOMContentLoaded", function() {
  // Exemple de données (dans une vraie application, ces données viendraient d'une API ou d'une base de données)
  const reviews = [
      { username: "John Smith", rating: 5, comment: "Great place, highly recommend!" },
      { username: "Jane Doe", rating: 4, comment: "Nice stay, but a bit noisy at night." }
  ];

  // Exemple d'état de connexion (pour simulation, cela pourrait venir de la gestion d'authentification)
  const isLoggedIn = false; // Si l'utilisateur est connecté ou non

  // Affichage des avis existants
  const reviewsList = document.getElementById("reviews-list");
  reviews.forEach(review => {
      const reviewCard = document.createElement("div");
      reviewCard.classList.add("review-card");
      reviewCard.innerHTML = `
          <p><strong>${review.username}</strong> - Rating: ${review.rating}/5</p>
          <p>${review.comment}</p>
      `;
      reviewsList.appendChild(reviewCard);
  });

  // Gestion de l'affichage du bouton ou du formulaire en fonction de la connexion
  const addReviewSection = document.getElementById("add-review-section");
  const addReviewButton = document.getElementById("add-review-button");
  const addReviewForm = document.getElementById("add-review-form");

  if (isLoggedIn) {
      // Afficher le formulaire d'ajout d'avis si l'utilisateur est connecté
      addReviewButton.style.display = "none";
      addReviewForm.style.display = "block";

      // Gestion de la soumission du formulaire d'avis
      addReviewForm.addEventListener("submit", function(event) {
          event.preventDefault();
          const comment = document.getElementById("review-comment").value;
          const rating = document.getElementById("review-rating").value;

          // Ajouter le nouvel avis à la liste
          const newReview = { username: "Current User", rating: rating, comment: comment };
          reviewsList.innerHTML = ""; // Réinitialiser la liste des avis
          reviews.push(newReview); // Ajouter le nouvel avis
          reviews.forEach(review => {
              const reviewCard = document.createElement("div");
              reviewCard.classList.add("review-card");
              reviewCard.innerHTML = `
                  <p><strong>${review.username}</strong> - Rating: ${review.rating}/5</p>
                  <p>${review.comment}</p>
              `;
              reviewsList.appendChild(reviewCard);
          });

          // Réinitialiser le formulaire
          addReviewForm.reset();
      });
  } else {
      // Si l'utilisateur n'est pas connecté, afficher un bouton pour ajouter un avis
      addReviewButton.style.display = "block";
      addReviewButton.addEventListener("click", function() {
          window.location.href = "add_review.html"; // Rediriger vers la page d'ajout d'avis
      });
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const loginForm = document.getElementById("login-form");
  const errorMessage = document.getElementById("error-message");

  // Écouteur d'événements pour la soumission du formulaire de connexion
  loginForm.addEventListener("submit", function (event) {
      event.preventDefault(); // Empêcher l'envoi standard du formulaire

      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;

      // Créer les données pour la requête AJAX
      const data = {
          email: email,
          password: password
      };

      // Faire une requête AJAX vers l'API pour tenter la connexion
      const xhr = new XMLHttpRequest();
      xhr.open("POST", "https://your-api-endpoint.com/login", true);
      xhr.setRequestHeader("Content-Type", "application/json");

      xhr.onreadystatechange = function () {
          if (xhr.readyState === XMLHttpRequest.DONE) {
              if (xhr.status === 200) {
                  // Connexion réussie, on obtient le JWT
                  const response = JSON.parse(xhr.responseText);
                  const token = response.token;

                  // Stocker le JWT dans un cookie
                  document.cookie = "jwt=" + token + "; path=/; max-age=3600"; // 1 heure de validité

                  // Rediriger vers la page principale
                  window.location.href = "index.html";
              } else {
                  // Afficher le message d'erreur si la connexion échoue
                  const error = JSON.parse(xhr.responseText);
                  errorMessage.textContent = error.message || "An error occurred. Please try again.";
                  errorMessage.style.display = "block";
              }
          }
      };

      // Envoyer la requête avec les données de connexion
      xhr.send(JSON.stringify(data));
  });
});
