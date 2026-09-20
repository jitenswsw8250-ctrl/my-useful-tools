package com.example

import android.content.Context
import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.junit4.createComposeRule
import androidx.compose.ui.test.onAllNodesWithText
import androidx.test.core.app.ApplicationProvider
import com.example.model.Screen
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.annotation.Config

@RunWith(RobolectricTestRunner::class)
@Config(sdk = [36])
class ExampleRobolectricTest {

  @get:Rule
  val composeTestRule = createComposeRule()

  @Test
  fun `read string from context`() {
    val context = ApplicationProvider.getApplicationContext<Context>()
    val appName = context.getString(R.string.app_name)
    assertEquals("MY USEFUL TOOLS", appName)
  }

  @Test
  fun `screen saver serialization works for all screens`() {
    val scope = object : androidx.compose.runtime.saveable.SaverScope {
      override fun canBeSaved(value: Any): Boolean = true
    }
    Screen.allScreens.forEach { screen ->
      val saved = with(Screen.Saver) { scope.save(screen) }
      assertNotNull("Saved route should not be null", saved)
      val restored = Screen.Saver.restore(saved!!)
      assertEquals("Restored screen should match original", screen, restored)
    }
  }

  @Test
  fun `app initializes and renders without crash`() {
    composeTestRule.setContent {
      MyUsefulToolsApp()
    }
    composeTestRule.onAllNodesWithText("MY USEFUL TOOLS")[0].assertIsDisplayed()
  }
}

