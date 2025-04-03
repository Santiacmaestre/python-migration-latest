import React from 'react'
import './HomePage.css'

export default function HomePage() {
  return (
    <div className="landing-container">
      <header className="landing-header">
        <div className="logo">EPAM ELITEA + CloudCrafters</div>
        <nav className="nav-links">
          <a href="#">About</a>
          <a href="#">Mission</a>
          <a href="#">Product</a>
          <button className="contact-btn">Contact</button>
        </nav>
      </header>

      <main className="landing-hero">
        <div className="hero-text">
          <h1>AI-powered Platform to Boost Enterprise Software Development</h1>
          <p>
              Automate business analysis, streamline development, and boost productivity using generative AI agents fully integrated with your enterprise tools.
          </p>
          <div className="hero-buttons">
            <a
              href="https://solutionshub.epam.com/solution/elitea"
              href="https://elitea.ai/"
              target="_blank"
              rel="noopener noreferrer"
              className="primary-btn how-it-works-btn"
            >
              Discover ELITEA
            </a>
          </div>
        </div>
        <div className="hero-image">
          <img src="/hero-illustration.png" alt="Developer Illustration" />
        </div>
      </main>
    </div>
  )
}
